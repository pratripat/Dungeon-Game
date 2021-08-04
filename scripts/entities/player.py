import pygame
from ..entity import Entity
from ..health_bar import Health_Bar

class Player(Entity):
    def __init__(self, game, rect):
        super().__init__(game.animations, 'player', list(rect.topleft), 'idle')
        self.game = game
        self.target_position = self.position.copy()
        self.health_bar = Health_Bar(self.game, [30, 30])
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}
        self.health = 5
        self.speed = 4
        self.invincible_timer = 0
        self.bleeding_timer = 0
        self.max_bleeding_timer = 500
        self.moving = False
        self.damaged = False

    def update(self):
        super().update(self.game.dt)
        self.movement()
        self.move(self.game.entity_manager.collidables, self.game.dt)

        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        if self.bleeding_timer > 0:
            self.bleeding_timer -= 1
            self.damage()

    def movement(self):
        if not(any(self.directions)):
            return

        if self.position == self.target_position:
            self.refresh()

        if self.directions['up']:
            self.velocity[1] -= 0.5
            self.velocity[1] = max(-self.speed, self.velocity[1])
        if self.directions['down']:
            self.velocity[1] += 0.5
            self.velocity[1] = min(self.speed, self.velocity[1])
        if self.directions['left']:
            self.flip(True)
            self.velocity[0] -= 0.5
            self.velocity[0] = max(-self.speed, self.velocity[0])
        if self.directions['right']:
            self.flip(False)
            self.velocity[0] += 0.5
            self.velocity[0] = min(self.speed, self.velocity[0])

    def render(self):
        super().render(self.game.screen, self.game.camera.scroll)

    def move_dir(self, dir):
        if self.moving:
            return

        self.refresh()

        self.directions[dir] = True
        self.moving = True

        if dir == 'up':
            self.target_position[1] -= self.game.tilemap.RES
        if dir == 'down':
            self.target_position[1] += self.game.tilemap.RES
        if dir == 'left':
            self.target_position[0] -= self.game.tilemap.RES
        if dir == 'right':
            self.target_position[0] += self.game.tilemap.RES

        for id in self.game.entity_manager.colliding_entity_ids:
            if len(self.game.tilemap.get_tiles_with_position(id, self.target_position)) > 0:
                self.refresh()
                break

    def damage(self):
        if self.invincible_timer > 0:
            return

        self.health -= 1

        self.damaged = True
        self.invincible_timer = 200

        if self.health == 0:
            self.game.over = True

    def bleed(self):
        self.bleeding_timer = self.max_bleeding_timer

    def refresh(self):
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}

        self.target_position[0] = self.rect[0] = self.rect[0]//self.game.tilemap.RES * self.game.tilemap.RES
        self.target_position[1] = self.rect[1] = self.rect[1]//self.game.tilemap.RES * self.game.tilemap.RES

        self.velocity = [0,0]

        self.moving = False

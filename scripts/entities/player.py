import pygame
from ..funcs import *
from ..entity import Entity
from ..health_bar import Health_Bar

class Player(Entity):
    def __init__(self, game, rect):
        super().__init__(game.animations, 'player', list(rect.topleft), 'idle')
        self.game = game
        self.target_position = self.position.copy()
        self.health_bar = Health_Bar(self.game, [30, 30])
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}
        self.health = self.max_health = 5
        self.speed = 4
        self.invincible_timer = 0
        self.bleeding_timer = 0
        self.max_bleeding_timer = 500
        self.moving = False
        self.damaged = False
        self.items = {}

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

        self.health_bar.render(self.health*10)

        for i, image in enumerate(self.items.values()):
            self.game.screen.blit(image, (i*(image.get_width()+20), 10))

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

        for rect in self.game.entity_manager.collidables:
            if rect_position_collision(rect, self.target_position):
                self.refresh()
                break

    def damage(self, value=1):
        if self.invincible_timer > 0:
            return

        self.health -= value

        self.damaged = True
        self.invincible_timer = 200

        if self.health == 0:
            self.game.over = True

    def bleed(self):
        self.bleeding_timer = self.max_bleeding_timer

    def increment_health(self, extra_health):
        self.health += extra_health

        if self.health > self.max_health:
            self.health = self.max_health

    def increment_invincibility(self, extra_invincibility):
        self.invincible_timer += extra_invincibility * 100

    def refresh(self):
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}

        self.target_position[0] = self.rect[0] = self.rect[0]//self.game.tilemap.RES * self.game.tilemap.RES
        self.target_position[1] = self.rect[1] = self.rect[1]//self.game.tilemap.RES * self.game.tilemap.RES

        self.velocity = [0,0]

        self.moving = False

    @property
    def dead(self):
        return self.health <= 0

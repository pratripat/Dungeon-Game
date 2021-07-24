import pygame
from ..entity import Entity

class Player(Entity):
    def __init__(self, game, rect):
        super().__init__(game.animations, 'player', list(rect.topleft), 'idle')
        self.game = game
        self.target_position = self.position.copy()
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}
        self.moving = False

    def update(self):
        super().update(self.game.dt)
        self.movement()
        self.move(self.game.entity_manager.collidables, self.game.dt)

    def movement(self):
        if not(any(self.directions)):
            return

        if self.position == self.target_position:
            self.refresh()

        if self.directions['up']:
            self.velocity[1] -= 0.5
            self.velocity[1] = max(-3, self.velocity[1])
        if self.directions['down']:
            self.velocity[1] += 0.5
            self.velocity[1] = min(3, self.velocity[1])
        if self.directions['left']:
            self.flip(True)
            self.velocity[0] -= 0.5
            self.velocity[0] = max(-3, self.velocity[0])
        if self.directions['right']:
            self.flip(False)
            self.velocity[0] += 0.5
            self.velocity[0] = min(3, self.velocity[0])

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
        self.game.over = True            

    def refresh(self):
        self.directions = {k:False for k in ['up', 'down', 'left', 'right']}

        self.target_position[0] = self.rect[0] = self.rect[0]//self.game.tilemap.RES * self.game.tilemap.RES
        self.target_position[1] = self.rect[1] = self.rect[1]//self.game.tilemap.RES * self.game.tilemap.RES

        self.velocity = [0,0]

        self.moving = False

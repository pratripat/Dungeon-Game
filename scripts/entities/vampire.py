from .enemy import Enemy
from ..funcs import *

class Vampire(Enemy):
    def __init__(self, game, rect):
        super().__init__(game, 'vampire', list(rect.topleft), 'idle')
        self.max_speed = 2

    def update(self):
        super().update()
        self.move_towards()

        #Makes player bleed on every touch
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.entity_manager.player.bleed()

    def move_towards(self):
        distance = (self.game.entity_manager.player.rect[0]-self.rect[0])**2 + (self.game.entity_manager.player.rect[1]-self.rect[1])**2
        if distance < (self.game.tilemap.RES*4)**2:
            self.velocity = [self.game.entity_manager.player.rect[0]-self.rect[0], self.game.entity_manager.player.rect[1]-self.rect[1]]
            self.velocity = normalize_vector(self.velocity, self.max_speed)
        else:
            self.velocity = [0, 0]

        self.move(self.game.entity_manager.collidables, self.game.dt)

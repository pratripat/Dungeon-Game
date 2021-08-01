from .enemy import Enemy
from ..funcs import *

class Skull(Enemy):
    def __init__(self, game, rect, velocity):
        super().__init__(game, 'skull', list(rect.topleft), 'moving')
        self.velocity = velocity
        self.remove = False

    def update(self):
        super().update()

        if self.remove:
            self.game.entity_manager.skulls.remove(self)

        self.rect[0] += self.velocity[0]
        self.rect[1] += self.velocity[1]

        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.remove = True

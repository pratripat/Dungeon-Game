from .enemy import Enemy
from ..funcs import *

class Vampire(Enemy):
    def __init__(self, game, rect):
        super().__init__(game, 'vampire', list(rect.topleft), 'idle')

    def update(self):
        super().update()

        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.entity_manager.player.bleed()

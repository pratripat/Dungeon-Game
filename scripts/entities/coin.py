from ..entity import Entity
from ..funcs import *

class Coin(Entity):
    def __init__(self, game, rect):
        super().__init__(game.animations, 'coin', list(rect.topleft), 'rotating')
        self.game = game

    def render(self):
        super().render(self.game.screen, self.game.camera.scroll)

    def update(self):
        super().update(self.game.dt)

        #Add coin to player and remove itself
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.entity_manager.coins.remove(self)
            self.game.entity_manager.player.coins += 1

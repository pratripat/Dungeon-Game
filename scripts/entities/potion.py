from ..entity import Entity
from ..funcs import *

class Potion(Entity):
    def __init__(self, game, id, rect):
        super().__init__(game.animations, id, list(rect.topleft), 'floating')
        self.game = game

    def render(self):
        super().render(self.game.screen, self.game.camera.scroll)

    def update(self, function):
        super().update(self.game.dt)

        #Performs given function when player touches the potion
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            function()

from ..entity import Entity
from ..funcs import *

class Enemy(Entity):
    def __init__(self, game, id, position, current_animation):
        super().__init__(game.animations, id, position, current_animation)
        self.id = id
        self.game = game

    def render(self):
        super().render(self.game.screen, self.game.camera.scroll)

    def update(self):
        super().update(self.game.dt)

        #Damages player when player touches enemy
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.entity_manager.player.damage()

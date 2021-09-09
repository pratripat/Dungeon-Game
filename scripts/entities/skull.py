from .enemy import Enemy
from ..funcs import *

class Skull(Enemy):
    def __init__(self, game, rect, velocity):
        super().__init__(game, 'skull', list(rect.topleft), 'moving')
        self.velocity = velocity
        self.remove = False

    def update(self):
        super().update()

        #Remove when asked to
        if self.remove:
            self.game.entity_manager.skulls.remove(self)

        #Move
        self.move(self.game.entity_manager.collidables, self.game.dt)

        if any(self.collisions.values()):
            self.remove = True

        #Damage player
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.remove = True

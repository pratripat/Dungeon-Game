from .enemy import Enemy
from .skull import Skull

class Skeleton(Enemy):
    def __init__(self, game, rect):
        super().__init__(game, 'skeleton', list(rect.topleft), 'idle')
        self.timer = self.max_timer = 3

    def update(self):
        super().update()

        #Adds flying skull in every direction periodically
        self.timer -= self.game.dt

        if self.timer <= 0:
            for velocity in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                skull = Skull(self.game, self.rect.copy(), velocity)
                self.game.entity_manager.skulls.append(skull)

            self.timer = self.max_timer

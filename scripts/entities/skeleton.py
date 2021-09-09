from .enemy import Enemy
from .skull import Skull

class Skeleton(Enemy):
    def __init__(self, game, rect):
        super().__init__(game, 'skeleton', list(rect.topleft), 'idle')
        self.timer = self.max_timer = 3

    def update(self):
        super().update()

        #Adds flying skull in every direction periodically
        if not self.on_screen:
            return
            
        self.timer -= self.game.dt

        if self.timer <= 0:
            for velocity in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                skull = Skull(self.game, self.rect.copy(), velocity)
                self.game.entity_manager.skulls.append(skull)

            self.timer = self.max_timer

    @property
    def on_screen(self):
        return not (
            self.rect[0] - self.game.camera.scroll[0] < 0 or
            self.rect[0] + self.rect[2] - self.game.camera.scroll[0] > self.game.screen.get_width() or
            self.rect[1] - self.game.camera.scroll[1] < 0 or
            self.rect[1] + self.rect[3] - self.game.camera.scroll[1] > self.game.screen.get_height()
        )

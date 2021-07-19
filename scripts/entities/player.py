import pygame
from ..entity import Entity

class Player(Entity):
    def __init__(self, game, rect):
        super().__init__(game.animations, 'player', list(rect.topleft), 'idle')
        self.game = game
        self.moving = False

    def update(self):
        super().update(self.game.dt)
        self.move([], self.game.dt)
        self.follow_mouse()

    def render(self):
        super().render(self.game.screen, self.game.camera.scroll)

    def follow_mouse(self):
        if not self.moving:
            return

        mouse_position = list(pygame.mouse.get_pos())
        mouse_position[0] += self.game.camera.scroll[0]
        mouse_position[1] += self.game.camera.scroll[1]

        self.rect[0] = mouse_position[0]
        self.rect[1] = mouse_position[1]

        self.set_moving(False)

    def set_moving(self, bool):
        self.moving = bool

import pygame
from .button import Button

class Restart_Button(Button):
    def __init__(self, game):
        self.game = game
        super().__init__(self.game, self.restart_button_image, (self.game.screen.get_width()//2-self.restart_button_image.get_width()//2, 150), self.game.load_cutscene, ['game_over', self.game.load_level])

    @property
    def restart_button_image(self):
        image = pygame.image.load('data/graphics/images/restart_button.png').convert()
        image = pygame.transform.scale(image, (image.get_width()*3, image.get_height()*3))
        image.set_colorkey((0, 0, 0))
        return image

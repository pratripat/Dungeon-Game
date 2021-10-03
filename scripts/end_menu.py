import pygame
from .funcs import *

class End_Menu:
    def __init__(self, game):
        self.game = game
        self.image = load_image('data/graphics/images/thanksforplaying.png', 3)
        self.running = False

    def load(self):
        self.running = True

    def render(self):
        self.game.render(update_screen=False)

        self.game.screen.blit(self.image, (self.game.screen.get_width()/2-self.image.get_width()/2, self.game.screen.get_height()/2-self.image.get_height()/2))
        self.game.cursor.render()

        pygame.display.update()

    def update(self):
        self.game.event_manager.update(player_movement=False, end_menu=True)

    def run(self):
        while self.running:
            self.update()
            self.render()

    def refresh(self):
        self.running = False
        self.game.running = False
        self.game.reset()
        pygame.event.clear()

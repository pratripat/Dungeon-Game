import pygame
from .funcs import *
from .restart_button import Restart_Button
from .resume_button import Resume_Button

class Pause_Menu:
    def __init__(self, game):
        self.game = game
        self.image = load_image('data/graphics/images/pause_menu_background.png', 3)

    def load(self):
        self.running = True
        self.load_buttons()
        self.run()

    def load_buttons(self):
        self.restart_button = Restart_Button(self.game)
        self.resume_button = Resume_Button(self.game)
        self.buttons = [self.restart_button, self.resume_button]

    def render(self):
        self.game.screen.blit(self.image, (self.game.screen.get_width()/2-self.image.get_width()/2, self.game.screen.get_height()/2-self.image.get_height()/2))
        for button in self.buttons:
            button.render()

        pygame.display.update()

    def update(self):
        self.game.event_manager.update(player_movement=False)

        for button in self.buttons:
            if button.update():
                self.refresh()

    def run(self):
        while self.running:
            self.update()
            self.render()

    def refresh(self):
        self.running = False
        pygame.event.clear()

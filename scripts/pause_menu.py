import pygame
from .restart_button import Restart_Button

class Pause_Menu:
    def __init__(self, game):
        self.game = game
        self.load_buttons()

    def load(self):
        self.running = True
        self.run()

    def load_buttons(self):
        self.restart_button = Restart_Button(self.game)
        self.buttons = [self.restart_button]

    def render(self):
        for button in self.buttons:
            button.render()

        pygame.display.update()

    def update(self):
        self.game.event_manager.update()

        for button in self.buttons:
            if button.update():
                self.refresh()

    def run(self):
        while self.running:
            self.update()
            self.render()

    def refresh(self):
        self.running = False

import pygame
from .funcs import *
from .restart_button import Restart_Button
from .resume_button import Resume_Button
from .sfx_disable_button import SFX_Disable_Button
from .music_disable_button import Music_Disable_Button

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
        self.sfx_disable_button = SFX_Disable_Button(self.game)
        self.music_disable_button = Music_Disable_Button(self.game)
        self.buttons = [self.restart_button, self.resume_button, self.sfx_disable_button, self.music_disable_button]

    def render(self):
        self.game.render(update_screen=False)
        self.game.screen.blit(self.image, (self.game.screen.get_width()/2-self.image.get_width()/2, self.game.screen.get_height()/2-self.image.get_height()/2))

        for button in self.buttons:
            button.render()

        self.game.cursor.render()

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

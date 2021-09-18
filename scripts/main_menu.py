import pygame
from .funcs import *
from .game import Game
from .play_button import Play_Button

class Main_Menu:
    def __init__(self):
        self.game = Game()
        self.load()

    def load(self):
        self.game_name_image = load_image('data/graphics/images/title.png', 3)
        self.running = True
        self.load_buttons()
        self.run()

    def load_buttons(self):
        self.play_button = Play_Button(self.game, self)
        self.buttons = [self.play_button]

    def start_game(self):
        self.game.level += 1
        self.game.load_cutscene('game_over', self.game.load_level)
        self.game.main_loop()

    def render(self):
        self.game.camera.scroll[1] = self.game.tilemap.bottom-self.game.screen.get_height()+self.game.tilemap.RES
        self.game.render(update_screen=False, render_timer=False)
        self.game.screen.blit(self.game_name_image, (self.game.screen.get_width()/2-self.game_name_image.get_width()/2, 100))

        for button in self.buttons:
            button.render()

        pygame.display.update()

    def update(self):
        self.game.update(player_movement=False, update_timer=False)

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

import pygame

class SFX_Manager:
    def __init__(self, game):
        self.game = game
        self.volume = 0.7
        self.disabled = False

    def play_sfx(self, filename):
        if self.disabled:
            return

        sfx = self.load_sfx(filename)
        sfx.play()

    def load_sfx(self, filename):
        if filename.split('.')[-1] != 'wav':
            filename += '.wav'

        filename = 'data/sfx/' + filename
        sfx = pygame.mixer.Sound(filename)
        sfx.set_volume(self.volume)
        return sfx

    def disable(self):
        self.disabled = not self.disabled

import pygame

class Music_Manager:
    def __init__(self, game):
        self.game = game
        self.volume = 1
        self.disabled = False
        self.current_music_filename = None
        self.current_music_loops = 1

    def play_music(self, filename, loop=1):
        if self.disabled:
            return

        self.load_music(filename)
        self.current_music_loops = loop
        pygame.mixer.music.play(loop)

    def load_music(self, filename):
        filename = self.get_actual_filepath(filename)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(self.volume)

    def add_to_queue(self, filename):
        if self.disabled:
            return

        pygame.mixer.music.queue(self.get_actual_filepath(filename))

    def get_actual_filepath(self, filename):
        if filename.split('.')[-1] != 'wav':
            filename += '.wav'

        self.current_music_filename = filename

        filename = 'data/music/' + filename

        return filename

    def disable(self):
        self.disabled = not self.disabled

        if self.disabled:
            pygame.mixer.music.pause()
            self.volume = 0
        else:
            pygame.mixer.music.unpause()
            self.volume = 1

    def stop(self):
        pygame.mixer.music.stop()        

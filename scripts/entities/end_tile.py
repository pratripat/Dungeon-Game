from ..funcs import *

class End_Tile:
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.id = 'end_tile'

    def render(self):
        pass

    def update(self):
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.level += 1
            self.game.load_cutscene('game_over', self.game.load_level)

from ..funcs import *

class End_Tile:
    def __init__(self, game, rect):
        self.game = game
        self.rect = rect
        self.id = 'end_tile'

    #Rendering is already handled by the renderer
    def render(self):
        pass

    #Load next level when player interacts with end tile
    def update(self):
        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            self.game.level += 1
            self.game.load_cutscene('game_over', self.game.load_level)

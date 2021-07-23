from .entities.player import Player
from .entities.torch import Torch

class Entity_Manager:
    def __init__(self, game):
        self.game = game
        self.load_entities()

    def load_entities(self):
        self.player = Player(self.game, self.game.tilemap.get_rects_with_id('player')[0])
        self.torches = [Torch(self.game, entity['index'], entity['position']) for entity in self.game.tilemap.get_tiles_with_id('torches')]

    def update(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        for entity in self.entities:
            entity.render()

    @property
    def entities(self):
        return [self.player, *self.torches]

    @property
    def collidables(self):
        collidables = []

        collidables.extend(self.game.tilemap.get_rects_with_id('walls'))
        collidables.extend(self.game.tilemap.get_rects_with_id('torches'))

        return collidables

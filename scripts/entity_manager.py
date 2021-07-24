from .entities.player import Player
from .entities.torch import Torch
from .entities.spike import Spike

class Entity_Manager:
    def __init__(self, game):
        self.game = game
        self.colliding_entity_ids = ['walls', 'torches']
        self.load_entities()

    def load_entities(self):
        self.player = Player(self.game, self.game.tilemap.get_rects_with_id('player')[0])
        self.torches = [Torch(self.game, entity['index'], entity['position']) for entity in self.game.tilemap.get_tiles_with_id('torches')]
        self.spikes = [Spike(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('spikes')]

    def update(self):
        if self.game.cutscene:
            return
            
        for entity in self.entities:
            entity.update()

    def render(self):
        for entity in self.entities:
            entity.render()

    @property
    def entities(self):
        return [*self.spikes, self.player, *self.torches]

    @property
    def collidables(self):
        collidables = []

        for id in self.colliding_entity_ids:
            collidables.extend(self.game.tilemap.get_rects_with_id(id))

        return collidables

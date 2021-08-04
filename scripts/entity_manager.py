from .entities.player import Player
from .entities.torch import Torch
from .entities.spike import Spike
from .entities.coin import Coin
from .entities.vampire import Vampire
from .entities.skeleton import Skeleton
from .entities.health_potion import Health_Potion

class Entity_Manager:
    def __init__(self, game):
        self.game = game
        self.colliding_entity_ids = ['walls', 'torches', 'decorations']
        self.load_entities()

    def load_entities(self):
        self.player = Player(self.game, self.game.tilemap.get_rects_with_id('player')[0])
        self.torches = [Torch(self.game, entity['index'], entity['position']) for entity in self.game.tilemap.get_tiles_with_id('torches')]
        self.spikes = [Spike(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('spikes')]
        self.coins = [Coin(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('coin')]
        self.skeletons = [Skeleton(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('skeleton')]
        self.vampires = [Vampire(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('vampire')]
        self.health_potions = [Health_Potion(self.game, 'small_health_potion', rect) for rect in self.game.tilemap.get_rects_with_id('small_health_potion')]+[Health_Potion(self.game, 'big_health_potion', rect) for rect in self.game.tilemap.get_rects_with_id('big_health_potion')]
        self.skulls = []

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
        return [*self.spikes, self.player, *self.torches, *self.coins, *self.enemies, *self.health_potions]

    @property
    def enemies(self):
        return [*self.vampires, *self.skeletons, *self.skulls]

    @property
    def collidables(self):
        collidables = []

        for id in self.colliding_entity_ids:
            collidables.extend(self.game.tilemap.get_rects_with_id(id))

        return collidables

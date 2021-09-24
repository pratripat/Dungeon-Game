from .entities.player import Player
from .entities.torch import Torch
from .entities.spike import Spike
from .entities.coin import Coin
from .entities.vampire import Vampire
from .entities.skeleton import Skeleton
from .entities.health_potion import Health_Potion
from .entities.invincibility_potion import Invincibility_Potion
from .entities.door import Door
from .entities.key import Key
from .entities.end_tile import End_Tile

class Entity_Manager:
    def __init__(self, game):
        self.game = game
        self.colliding_entity_ids = ['walls', 'torches', 'decorations', 'silver_door', 'gold_door']
        self.load_entities()

    def load_entities(self):
        self.player = Player(self.game, self.game.tilemap.get_rects_with_id('player')[0])
        self.torches = [Torch(self.game, entity['index'], entity['position']) for entity in self.game.tilemap.get_tiles_with_id('torches')]
        self.spikes = [Spike(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('spikes')]
        self.coins = [Coin(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('coin')]
        self.skeletons = [Skeleton(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('skeleton')]
        self.vampires = [Vampire(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('vampire')]
        self.health_potions = [Health_Potion(self.game, 'small_health_potion', rect) for rect in self.game.tilemap.get_rects_with_id('small_health_potion')]+[Health_Potion(self.game, 'big_health_potion', rect) for rect in self.game.tilemap.get_rects_with_id('big_health_potion')]
        self.invincibility_potions = [Invincibility_Potion(self.game, 'small_invincibility_potion', rect) for rect in self.game.tilemap.get_rects_with_id('small_invincibility_potion')]+[Invincibility_Potion(self.game, 'big_invincibility_potion', rect) for rect in self.game.tilemap.get_rects_with_id('big_invincibility_potion')]
        self.doors = [Door(self.game, 'silver_door', rect) for rect in self.game.tilemap.get_rects_with_id('silver_door')]+[Door(self.game, 'gold_door', rect) for rect in self.game.tilemap.get_rects_with_id('gold_door')]+[End_Tile(self.game, rect) for rect in self.game.tilemap.get_rects_with_id('end_tile')]
        self.keys = [Key(self.game, 'silver_key', rect) for rect in self.game.tilemap.get_rects_with_id('silver_key')]+[Key(self.game, 'gold_key', rect) for rect in self.game.tilemap.get_rects_with_id('gold_key')]
        self.skulls = []

    def update(self):
        #Return if cutscene is being played currently
        if self.game.cutscene:
            return

        #Updating all the entities
        for entity in self.entities:
            entity.update()

        if self.player.dead:
            self.game.over = True
            self.game.music_manager.play_music('player_death')
            self.game.music_manager.add_to_queue('main_music')

    def render(self):
        #Rendering all the entities
        for entity in self.entities:
            entity.render()

    #Returns a list of all entities
    @property
    def entities(self):
        return [*self.spikes, self.player, *self.torches, *self.coins, *self.enemies, *self.health_potions, *self.invincibility_potions, *self.doors, *self.keys]

    #Returns a list of all enemies
    @property
    def enemies(self):
        return [*self.vampires, *self.skeletons, *self.skulls]

    #Returns a list of all tiles that player cannot go through
    @property
    def collidables(self):
        collidables = []

        for id in self.colliding_entity_ids:
            collidables.extend(self.game.tilemap.get_rects_with_id(id))

        return collidables

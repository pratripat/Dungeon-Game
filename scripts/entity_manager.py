from .entities.player import Player

class Entity_Manager:
    def __init__(self, game):
        self.game = game
        self.load_entities()

    def load_entities(self):
        self.player = Player(self.game, self.game.tilemap.get_rects_with_id('player')[0])

    def update(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        for entity in self.entities:
            entity.render()

    @property
    def entities(self):
        return [self.player]

from ..entity import Entity

class Player(Entity):
    def __init__(self, game, rect=None):
        super().__init__(game.animations, 'player', [16, 16], 'idle')
        self.game = game

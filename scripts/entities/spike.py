class Spike:
    def __init__(self, game, rect):
        self.game = game
        self.position = list(rect.topleft)
        self.animation = self.game.animations.get_animation('spikes')

    def render(self):
        self.animation.render(self.game.screen, [self.position[0]-self.game.camera.scroll[0], self.position[1]-self.game.camera.scroll[1]])

    def update(self):
        self.animation.run(self.game.dt)
        self.damage_player()

    def damage_player(self):
        if 30 < self.animation.frame < 71:
            return

        if self.game.entity_manager.player.position == self.position:
            self.game.entity_manager.player.damage()

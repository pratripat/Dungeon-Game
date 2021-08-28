class Timer:
    def __init__(self, game):
        self.game = game
        self.time = 61

    def render(self):
        if self.time > 60:
            time = f'{int(self.time)//60:02d}:{int(self.time-60):02d}'
        else:
            time = f'00:{int(self.time):02d}'

        self.game.font.render(self.game.screen, time, [self.game.screen.get_width()-150, 30], scale=3)

    def update(self):
        self.time -= self.game.dt

        if self.time <= 0:
            self.time = 0
            self.game.entity_manager.player.damage(self.game.entity_manager.player.health)

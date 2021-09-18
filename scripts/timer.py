class Timer:
    def __init__(self, game):
        self.game = game
        self.time = 61

    #Renders time left before player dies
    def render(self):
        if self.time > 60:
            time = f'{int(self.time)//60:02d}:{int(self.time-60):02d}'
        else:
            time = f'00:{int(self.time):02d}'

        font_surface = self.game.font.get_text_surface(time, scale=3)
        self.game.screen.blit(font_surface, [self.game.screen.get_width()//2-font_surface.get_width()//2, 90])

    #Decrements timers by one every second
    def update(self):
        if self.game.dt == 0 or 1/self.game.dt < 20:
            return

        if self.game.entity_manager.player.coins == 50:
            self.time += 10
            self.game.entity_manager.player.coins = 0

        self.time -= self.game.dt

        if self.time <= 0:
            self.time = 0
            self.game.entity_manager.player.instant_kill()

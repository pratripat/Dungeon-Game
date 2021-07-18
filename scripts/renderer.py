import pygame

class Renderer:
    def __init__(self, game):
        self.game = game
        self.entities = ['walls', 'tiles']
        self.background_color = (0,0,0)

    def render(self):
        self.game.screen.fill(self.background_color)

        for entity in self.game.tilemap.entities:
            if entity['id'] in self.entities:
                self.game.screen.blit(entity['image'], (entity['position'][0]-self.game.camera.scroll[0], entity['position'][1]-self.game.camera.scroll[1]))

        pygame.display.update()

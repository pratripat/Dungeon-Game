import pygame

class Renderer:
    def __init__(self, game):
        self.game = game
        self.entities = ['walls', 'tiles', 'decorations']
        self.background_color = (37, 19, 26)

    def render(self):
        self.game.screen.fill(self.background_color)

        for entity in self.game.tilemap.entities:
            if entity['id'] in self.entities:
                self.game.screen.blit(entity['image'], (entity['position'][0]-self.game.camera.scroll[0], entity['position'][1]-self.game.camera.scroll[1]))

        self.game.entity_manager.render()

        for rect in self.game.entity_manager.collidables:
            pygame.draw.rect(self.game.screen, (255,0,0), (rect[0]-self.game.camera.scroll[0], rect[1]-self.game.camera.scroll[1], rect[2], rect[3]))

        self.game.entity_manager.player.health_bar.render(self.game.entity_manager.player.health*10)

        self.game.level_transition_rect.render()

        self.game.font.render(self.game.screen, str(self.game.dt*10000), [10, 200])

        pygame.display.update()

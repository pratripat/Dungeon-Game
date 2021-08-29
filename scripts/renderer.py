import pygame

class Renderer:
    def __init__(self, game):
        self.game = game
        self.entities = ['walls', 'tiles', 'decorations', 'end_tile']
        self.background_color = (37, 19, 26)

    def render(self):
        #Background color is rendered
        self.game.screen.fill(self.background_color)

        #All of tilemap entities are rendered
        for entity in self.game.tilemap.entities:
            if entity['id'] in self.entities:
                self.game.screen.blit(entity['image'], (entity['position'][0]-self.game.camera.scroll[0], entity['position'][1]-self.game.camera.scroll[1]))

        #All entities are rendered
        self.game.entity_manager.render()

        #Time left is rendered
        self.game.timer.render()

        # for rect in self.game.entity_manager.collidables:
        #     pygame.draw.rect(self.game.screen, (255,0,0), (rect[0]-self.game.camera.scroll[0], rect[1]-self.game.camera.scroll[1], rect[2], rect[3]))

        #Level transition rect (black rect) is rendered
        self.game.level_transition_rect.render()

        #Temp rendering of fps
        self.game.font.render(self.game.screen, str(self.game.dt*10000), [10, 200])

        pygame.display.update()

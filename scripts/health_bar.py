import pygame

class Health_Bar:
    def __init__(self, game, position):
        self.game = game
        self.position = position
        self.color = (188, 76, 82)
        self.scale = 3
        self.image = pygame.image.load('data/graphics/images/health_bar.png').convert()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*self.scale, self.image.get_height()*self.scale))
        self.image.set_colorkey((0, 0, 0))

    def render(self, health):
        pygame.draw.rect(self.game.screen, self.color, (self.position[0]+self.scale, self.position[1], health*self.scale, self.image.get_height()))
        self.game.screen.blit(self.image, self.position)

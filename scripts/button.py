import pygame

class Button:
    def __init__(self, game, image, position, function, args=[]):
        self.game = game
        self.image = image
        self.position = position
        self.function = function
        self.args = args

    def render(self):
        self.game.screen.blit(self.image, self.position)

    def update(self):
        if not self.mouse_hovering:
            return False

        if not pygame.mouse.get_pressed()[0]:
            return False

        self.function(*self.args)
        return True

    @property
    def mouse_hovering(self):
        mouse_pos = pygame.mouse.get_pos()

        return (
            self.position[0] < mouse_pos[0] < self.position[0]+self.image.get_width() and
            self.position[1] < mouse_pos[1] < self.position[1]+self.image.get_height()
        )

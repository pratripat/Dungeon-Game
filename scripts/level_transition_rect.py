import pygame

class Level_Transition_Rect:
    def __init__(self, game):
        self.game = game
        # self.color = (37, 19, 26)
        self.color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, self.game.screen.get_width()+10, self.game.screen.get_height())
        self.moving = False

    def set_left(self):
        if self.moving:
            return

        self.rect[0] = 0
        self.moving = True

    def set_right(self):
        if self.moving:
            return

        self.rect[0] = -self.rect[2]
        self.moving = True

    def render(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)

    def move_rect_left(self):
        self.rect[0] -= 10

    def move_rect_right(self):
        self.rect[0] += 10

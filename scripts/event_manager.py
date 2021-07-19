import pygame, sys

class Event_Manager:
    def __init__(self, game):
        self.game = game

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.entity_manager.player.set_moving(True)
            if event.type == pygame.MOUSEBUTTONUP:
                self.game.entity_manager.player.set_moving(False)

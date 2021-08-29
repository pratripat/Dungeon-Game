import pygame, sys

class Event_Manager:
    def __init__(self, game):
        self.game = game

    def update(self):
        #Return if cutscene is being played currently
        if self.game.cutscene:
            return

        for event in pygame.event.get():
            #Quiting when the exit button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #Quiting when the escape button is clicked
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                #Moving player when arrow keys or wasd keys are pressed    
                if event.key in [pygame.K_w, pygame.K_UP]:
                    self.game.entity_manager.player.move_dir('up')
                elif event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.game.entity_manager.player.move_dir('left')
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.game.entity_manager.player.move_dir('down')
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.game.entity_manager.player.move_dir('right')

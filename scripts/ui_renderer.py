import pygame

class UI_Renderer:
    def __init__(self, game):
        self.game = game
        self.inventory_image = pygame.image.load('data/graphics/images/inventory.png').convert()
        self.inventory_image = pygame.transform.scale(self.inventory_image, (self.inventory_image.get_width()*3, self.inventory_image.get_height()*3))
        self.inventory_image.set_colorkey((0, 0, 0))

    def render(self):
        #Render health bar
        self.game.entity_manager.player.health_bar.render(self.game.entity_manager.player.health)
        self.game.timer.render()

        #Temp rendering of fps
        self.game.font.render(self.game.screen, str(1/(self.game.dt+0.00001)), [10, 200])

        width = self.inventory_image.get_width()*len(self.game.entity_manager.player.items.values())
        height = self.inventory_image.get_height()

        item_surface = pygame.Surface((width, height))
        item_surface.set_colorkey((0, 0, 0))

        # Render items
        for i, image in enumerate(self.game.entity_manager.player.items.values()):
            item_surface.blit(self.inventory_image, (i*self.inventory_image.get_width(), 0))
            item_surface.blit(image, (i*self.inventory_image.get_width()+3, 0))

        self.game.screen.blit(item_surface, (self.game.entity_manager.player.health_bar.position[0], self.game.entity_manager.player.health_bar.position[1]+item_surface.get_height()*1.5))

        #Render pause button
        self.game.pause_button.render()

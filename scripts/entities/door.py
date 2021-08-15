from ..funcs import *

class Door:
    def __init__(self, game, id, rect):
        self.game = game
        self.id = id
        self.rect = rect
        self.image = load_images_from_spritesheet('data/graphics/spritesheet/doors.png')[{'silver_door': 0, 'gold_door': 1}[self.id]]
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))

    def render(self):
        self.game.screen.blit(self.image, (self.rect[0]-self.game.camera.scroll[0], self.rect[1]-self.game.camera.scroll[1]))

    def update(self):
        pass

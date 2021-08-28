from ..funcs import *

class Door:
    def __init__(self, game, id, rect):
        self.game = game
        self.id = id
        self.rect = rect
        self.image = load_images_from_spritesheet('data/graphics/spritesheet/entities.png')[{'silver_door': 9, 'gold_door': 10}[self.id]]
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))

    def render(self):
        self.game.screen.blit(self.image, (self.rect[0]-self.game.camera.scroll[0], self.rect[1]-self.game.camera.scroll[1]))

    def update(self):
        id = self.id.split('_')[0]+'_key'

        if id in self.game.entity_manager.player.items.keys():
            if self.game.entity_manager.player.rect[1] in [self.rect[1]-self.rect[3], self.rect[1]+self.rect[3]] and self.game.entity_manager.player.rect[0] in [self.rect[0], self.rect[0]+self.rect[2]//2]:
                self.game.entity_manager.doors.remove(self)
                del self.game.entity_manager.player.items[id]

                for entity in self.game.tilemap.entities:
                    if entity['position'] == list(self.rect.topleft) and entity['id'] == self.id:
                        self.game.tilemap.entities.remove(entity)
                        break

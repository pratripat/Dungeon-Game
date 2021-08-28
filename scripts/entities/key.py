from ..funcs import *

class Key:
    def __init__(self, game, id, rect):
        self.game = game
        self.id = id
        self.rect = rect
        self.animation = self.game.animations.get_animation(self.id)

    def render(self):
        self.animation.render(self.game.screen, (self.rect[0]-self.game.camera.scroll[0], self.rect[1]-self.game.camera.scroll[1]))

    def update(self):
        self.animation.run(self.game.dt)

        if rect_rect_collision(self.rect, self.game.entity_manager.player.rect):
            image = self.animation.animation_data.images[0]
            scale = self.animation.animation_data.config['scale']
            self.game.entity_manager.player.items[self.id] = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
            self.game.entity_manager.keys.remove(self)

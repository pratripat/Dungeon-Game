from ..funcs import *

class Torch:
    def __init__(self, game, index, position):
        self.game = game
        self.index = index
        self.position = position
        self.load_animation()

    def load_animation(self):
        #Loads appropriate animation according to the index in spritesheet
        if self.index == 6:
            self.animation = self.game.animations.get_animation('torch_1')
        elif self.index == 7:
            self.animation = self.game.animations.get_animation('torch_2')
        elif self.index == 9:
            self.animation = self.game.animations.get_animation('torch_3')
        elif self.index == 11:
            self.animation = self.game.animations.get_animation('torch_4')
        else:
            self.animation = create_new_animation('data/graphics/animations/torch_1', [load_images_from_spritesheet('data/graphics/spritesheet/decorations.png')[self.index]], True, 3)

    def render(self):
        self.animation.render(self.game.screen, [self.position[0]-self.game.camera.scroll[0], self.position[1]-self.game.camera.scroll[1]])

    def update(self):
        self.animation.run(self.game.dt)

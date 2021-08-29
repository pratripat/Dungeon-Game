import pygame
from ..funcs import *

class Spike:
    def __init__(self, game, rect):
        self.game = game
        self.position = list(rect.topleft)
        self.animation = self.game.animations.get_animation('spikes')

    def render(self):
        self.animation.render(self.game.screen, [self.position[0]-self.game.camera.scroll[0], self.position[1]-self.game.camera.scroll[1]])

    def update(self):
        self.animation.run(self.game.dt)
        self.damage_entity()

    def damage_entity(self):
        if 30 < self.animation.frame < 71:
            return

        #When spike if out and player is at the same position as spike, damage player
        for entity in [self.game.entity_manager.player, *self.game.entity_manager.enemies]:
            if rect_rect_collision(entity.rect, pygame.Rect(*self.position, self.game.tilemap.RES, self.game.tilemap.RES)):
                entity.damage()

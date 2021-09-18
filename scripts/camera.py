import random

class Camera:
    def __init__(self, game, target=None):
        self.game = game
        self.target = target
        self.scroll = [100,0]
        self.time = 0
        self.movement = 1
        self.screen_shake = 0

    def update(self, tilemap=None):
        if self.time == 0:
            self.screen_shake = 0

        #Moves camera towards target
        if self.target:
            self.scroll[0] += int((self.target.center[0]-self.scroll[0]-self.game.screen.get_width()/2) * self.movement + random.uniform(-self.screen_shake, self.screen_shake+1))
            self.scroll[1] += int((self.target.center[1]-self.scroll[1]-self.game.screen.get_width()/2) * self.movement + random.uniform(-self.screen_shake, self.screen_shake+1))

        if self.time > 0:
            self.time -= 1

        #Keeps camera within the tilemap constraints
        if tilemap:
            if self.scroll[0] > tilemap.right-self.game.screen.get_width()+tilemap.RES:
                self.scroll[0] = tilemap.right-self.game.screen.get_width()+tilemap.RES
            if self.scroll[0] < tilemap.left:
                if tilemap.right-tilemap.left > self.game.screen.get_width():
                    self.scroll[0] = tilemap.left
                else:
                    self.scroll[0] = self.target.center[0]-self.game.screen.get_width()/2
            if self.scroll[1] < tilemap.top:
                self.scroll[1] = tilemap.top
            if self.scroll[1] > tilemap.bottom-self.game.screen.get_height()+tilemap.RES:
                self.scroll[1] = tilemap.bottom-self.game.screen.get_height()+tilemap.RES

    def set_target(self, target):
        self.target = target

    def set_movement(self, movement):
        self.movement = movement

    def set_screen_shake(self, screen_shake, time):
        self.screen_shake = screen_shake
        self.time = time

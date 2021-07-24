import json, pygame
from .camera import Camera
from .tilemap import Tilemap
from .renderer import Renderer
from .event_manager import Event_Manager
from .entity_manager import Entity_Manager
from .animation_handler import Animation_Handler
from .cutscene import Cutscene

class Game:
    def __init__(self):
        self.window_size = (1000,700)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE+pygame.SCALED)
        self.clock = pygame.time.Clock()

        self.screen.set_alpha(255)

        self.level = 0
        self.level_order = json.load(open('data/configs/levels/level_order.json', 'r'))

        self.load_level()

        self.camera = Camera(self)
        self.renderer = Renderer(self)
        self.event_manager = Event_Manager(self)
        self.animations = Animation_Handler()
        self.entity_manager = Entity_Manager(self)

        self.camera.set_target(self.entity_manager.player)
        self.camera.set_movement(0.05)

    def load_level(self):
        self.over = False
        self.cutscene = None
        self.tilemap = Tilemap(self.level_order[self.level])

        try:
            self.entity_manager.load_entities()

            self.camera.set_target(self.entity_manager.player)
            self.camera.set_movement(0.05)
        except:
            pass

    def update(self):
        self.clock.tick()

        self.camera.update()
        self.update_cutscene()
        self.event_manager.update()
        self.entity_manager.update()

        if self.over:
            self.load_cutscene('game_over', self.load_level)

    def render(self):
        self.renderer.render()

    def main_loop(self):
        while True:
            self.update()
            self.render()

    def update_cutscene(self):
        if not self.cutscene:
            return

        self.cutscene.update()
        if self.cutscene.finished:
            self.cutscene = None

    def game_over_screen(self):
        self.screen.set_alpha(self.screen.get_alpha()-1)

    def game_begin_screen(self):
        self.screen.set_alpha(self.screen.get_alpha()+1)

    def load_cutscene(self, path, function=None, args=[]):
        data = json.load(open(f'data/cutscenes/{path}.json', 'r'))
        self.cutscene = Cutscene(self, data['sequential_commands'], data['independent_commands'], function, args)

    @property
    def dt(self):
        if self.clock.get_fps() == 0:
            return 0

        return 1/self.clock.get_fps()

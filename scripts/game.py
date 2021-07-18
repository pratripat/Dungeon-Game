import json, pygame
from .camera import Camera
from .tilemap import Tilemap
from .renderer import Renderer
from .event_manager import Event_Manager
from .entity_manager import Entity_Manager

class Game:
    def __init__(self):
        self.window_size = (1000,700)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE+pygame.SCALED)

        self.level = 0
        self.level_order = json.load(open('data/configs/levels/level_order.json', 'r'))

        self.camera = Camera(self)
        self.renderer = Renderer(self)
        self.event_manager = Event_Manager(self)
        self.entity_manager = Entity_Manager(self)

        self.load_level()

    def load_level(self):
        self.tilemap = Tilemap(self.level_order[self.level])
        self.entity_manager.load_entities()

    def update(self):
        self.camera.update()
        self.event_manager.update()
        self.entity_manager.update()

    def render(self):
        self.renderer.render()

    def main_loop(self):
        while True:
            self.update()
            self.render()

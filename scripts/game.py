import json, pygame
from .font import Font
from .timer import Timer
from .camera import Camera
from .tilemap import Tilemap
from .renderer import Renderer
from .cutscene import Cutscene
from .pause_menu import Pause_Menu
from .end_menu import End_Menu
from .pause_button import Pause_Button
from .event_manager import Event_Manager
from .entity_manager import Entity_Manager
from .animation_handler import Animation_Handler
from .level_transition_rect import Level_Transition_Rect
from .sfx_manager import SFX_Manager
from .music_manager import Music_Manager
from .cursor import Cursor

pygame.init()
pygame.mouse.set_visible(False)

class Game:
    def __init__(self):
        self.window_size = (1000,700)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE+pygame.SCALED)
        pygame.display.set_caption('Dungeon master')
        self.clock = pygame.time.Clock()

        self.level = 0
        self.level_order = json.load(open('data/configs/levels/level_order.json', 'r'))
        self.cutscene = None
        self.end_level = False

        self.load_level()

        #All important objects
        self.cursor = Cursor(self)
        self.camera = Camera(self)
        self.renderer = Renderer(self)
        self.event_manager = Event_Manager(self)
        self.animations = Animation_Handler()
        self.entity_manager = Entity_Manager(self)
        self.font = Font('data/graphics/spritesheet/font.png')
        self.level_transition_rect = Level_Transition_Rect(self)
        self.pause_menu = Pause_Menu(self)
        self.pause_button = Pause_Button(self)
        self.end_menu = End_Menu(self)

        self.sfx_manager = SFX_Manager(self)
        self.music_manager = Music_Manager(self)

        #Sets player as the target
        self.camera.set_target(self.entity_manager.player)
        self.camera.set_movement(0.05)

        self.player_data = self.entity_manager.player.get_player_data()

    def load_level(self):
        self.over = False
        self.timer = Timer(self)

        try:
            self.tilemap = Tilemap(self.level_order[self.level])
        except:
            self.tilemap = Tilemap('data/levels/end.json')
            self.end_level = True

        try:
            self.player_data = self.entity_manager.player.get_player_data()

            if self.player_data['health'] == 0:
                self.player_data['health'] = self.entity_manager.player.max_health

            self.pause_menu.refresh()
            self.entity_manager.load_entities()

            self.camera.set_target(self.entity_manager.player)
            self.camera.set_movement(0.05)
        except:
            pass

        #First cutscene (black rect moving)
        if self.end_level:
            self.load_cutscene('game_begin', self.end_menu.load)
        else:
            self.load_cutscene('game_begin')

        pygame.event.clear()

    def update(self, player_movement=True, update_timer=True, pause_button=True):
        #Fps
        self.clock.tick(100)

        #Updating the objects
        self.camera.update(self.tilemap)
        self.update_cutscene()
        self.event_manager.update(player_movement=player_movement)
        self.entity_manager.update()
        self.end_menu.run()

        if pause_button:
            self.pause_button.update()

        if not self.entity_manager.player.dead and update_timer:
            self.timer.update()

        if self.over:
            self.load_cutscene('game_over', self.load_level)

    def render(self, update_screen=True, render_timer=True, pause_button=True):
        self.renderer.render(update_screen, render_timer, pause_button)

    def main_loop(self):
        self.running = True
        self.music_manager.play_music('main_music', -1)
        while self.running:
            self.update()
            self.render()

    def update_cutscene(self):
        #Update cutscene is it is playing (or return)
        if not self.cutscene:
            return

        self.cutscene.update()
        if self.cutscene.finished:
            self.cutscene = None

    def game_over_screen(self):
        self.level_transition_rect.set_right()
        self.level_transition_rect.move_rect_right()

    def game_begin_screen(self):
        self.level_transition_rect.set_left()
        self.level_transition_rect.move_rect_left()

    def load_cutscene(self, path, function=None, args=[]):
        data = json.load(open(f'data/cutscenes/{path}.json', 'r'))
        self.cutscene = Cutscene(self, data['sequential_commands'], data['independent_commands'], function, args)
        self.over = False

    def set_running(self, bool):
        self.running = bool

    def reset(self):
        self.level = 0
        self.end_level = False

        self.tilemap = Tilemap(self.level_order[self.level])
        self.pause_menu.refresh()

        self.player_data['coins'] = 0
        self.player_data['health'] = self.entity_manager.player.max_health

        self.entity_manager = Entity_Manager(self)

        self.camera.set_target(self.entity_manager.player)
        self.camera.set_movement(0.05)

        self.music_manager.stop()

    @property
    def dt(self):
        if self.clock.get_fps() == 0:
            return 0

        return 1/self.clock.get_fps()

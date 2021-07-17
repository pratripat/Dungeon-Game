import pygame, sys
from .world.world import World
from .selection_panel.selection_panel import Selection_Panel
from .font_renderer import Font

class Editor:
    def __init__(self):
        pygame.display.set_caption('Level Editor')

        self.screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.font = Font('data/graphics/spritesheet/leveleditor_font')
        self.res = 48
        self.world = World(self)
        self.selection_panel = Selection_Panel(self)

    @property
    def dt(self):
        fps = self.clock.get_fps()
        if fps == 0:
            return 0

        return 1/fps

    def load(self, filename):
        self.world.load(filename)

    def render(self, mouse_position):
        self.screen.fill((13,19,42))

        self.world.render()
        self.world.render_current_selection(mouse_position, self.selection_panel.get_current_selection())
        self.selection_panel.render()
        self.render_mouse_location(mouse_position)

        pygame.display.update()

    def run(self):
        self.clock.tick()

        keys = pygame.key.get_pressed()
        mouse_clicks = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()

        if keys[pygame.K_w]:
            self.world.scroll[1] -= 700 * self.dt
        if keys[pygame.K_a]:
            self.world.scroll[0] -= 700 * self.dt
        if keys[pygame.K_s]:
            self.world.scroll[1] += 700 * self.dt
        if keys[pygame.K_d]:
            self.world.scroll[0] += 700 * self.dt

        if not self.selection_panel.is_mouse_hovering(mouse_position):
            self.world.run(mouse_clicks[0], mouse_position, self.selection_panel.get_current_selection())
            self.world.create_rectangle(mouse_position, mouse_clicks[2])

        if keys[pygame.K_DELETE]:
            self.world.delete()

        ctrl_key = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]

        if ctrl_key and mouse_clicks[0]:
            self.world.fill(mouse_position, self.selection_panel.get_current_selection())
        if ctrl_key and keys[pygame.K_z]:
            self.world.undo()
        if ctrl_key and keys[pygame.K_c]:
            self.world.copy()
        if ctrl_key and keys[pygame.K_v]:
            self.world.paste(mouse_position)
        if ctrl_key and keys[pygame.K_t]:
            self.world.autotile(self.selection_panel)
        if ctrl_key and keys[pygame.K_s]:
            self.world.save()

        self.render(mouse_position)

    def render_mouse_location(self, mouse_position):
        self.font.render(self.screen, f'{int((mouse_position[0]+self.world.scroll[0])//self.res)};{int((mouse_position[1]+self.world.scroll[1])//self.res)}', [320, 10], color=(173,195,232))
        self.font.render(self.screen, f'{int((mouse_position[0]+self.world.scroll[0])//self.res)*self.res};{int((mouse_position[1]+self.world.scroll[1])//self.res)*self.res}', [320, 30], color=(173,195,232))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selection_panel.update_on_mouse_click(event.pos)
                self.world.update(self.selection_panel.get_current_selection())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_UP:
                    self.world.add_layer(-1)
                if event.key == pygame.K_DOWN:
                    self.world.add_layer(1)

    def main_loop(self):
        while True:
            self.event_loop()
            self.run()

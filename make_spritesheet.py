import pygame
from scripts.funcs import *

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
'''
images = [
    pygame.image.load('data/graphics/spritesheet/player.png'),
    pygame.image.load('data/graphics/spritesheet/coin.png'),
    pygame.image.load('data/graphics/spritesheet/skull.png'),
    pygame.image.load('data/graphics/spritesheet/skeleton.png'),
    pygame.image.load('data/graphics/spritesheet/vampire.png'),
    pygame.image.load('data/graphics/spritesheet/small_health_potion.png'),
    pygame.image.load('data/graphics/spritesheet/big_health_potion.png'),
    pygame.image.load('data/graphics/spritesheet/small_invincibility_potion.png'),
    pygame.image.load('data/graphics/spritesheet/big_invincibility_potion.png')
]

spritesheets = [
    'data/graphics/spritesheet/doors.png',
    'data/graphics/spritesheet/keys.png'
]

for spritesheet in spritesheets:
    spritesheet_images = load_images_from_spritesheet(spritesheet)
    images.extend(spritesheet_images)

surf = pygame.Surface((sum([image.get_width() for image in images])+(len(images)*2)+1, max([image.get_height() for image in images])+2))
surf.set_at((0,0), (0,0,255))
position = [1,1]

for i, image in enumerate(images):
    surf.set_at((position[0], position[1]-1), (255,255,0))
    position[0] += 1

    # img = pygame.Surface(rect.size)
    # img.blit(ORIGINAL_IMAGE, (-rect[0], -rect[1]))

    surf.blit(image, position)

    surf.set_at((position[0]+image.get_width(), position[1]), (255,0,255))
    surf.set_at((position[0], position[1]+image.get_height()), (255,0,255))

    position[0] += image.get_width()+1

# pygame.image.save(surf, 'data/graphics/spritesheet/entities.png')
'''

spritesheet = pygame.image.load('data/graphics/spritesheet/tileset.png')
image = pygame.image.load('data/graphics/spritesheet/end_tile.png')

surface = pygame.Surface((spritesheet.get_width()+image.get_width()+2, spritesheet.get_height()))

surface.blit(spritesheet, (0,0))
surface.blit(image, (spritesheet.get_width()+1, 1))

surface.set_at((spritesheet.get_width(), 0), (255, 255, 0))
surface.set_at((spritesheet.get_width()+1, image.get_height()+1), (255, 0, 255))
surface.set_at((surface.get_width()-1, 1), (255, 0, 255))

# pygame.image.save(surface, 'data/graphics/spritesheet/temp_spritesheet.png')

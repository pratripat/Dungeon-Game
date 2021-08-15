import pygame
from .animation_handler import Animation_Data, Animation

def load_images_from_spritesheet(filename):
    #Tries to load the file
    try:
        spritesheet = pygame.image.load(filename).convert()
    except Exception as e:
        print('LOADING SPRITESHEET ERROR: ', e)
        return []

    rows = []
    images = []

    for y in range(spritesheet.get_height()):
        pixil = spritesheet.get_at((0, y))
        if pixil[2] == 255:
            rows.append(y)

    for row in rows:
        for x in range(spritesheet.get_width()):
            start_position = []
            pixil = spritesheet.get_at((x, row))
            if pixil[0] == 255 and pixil[1] == 255 and pixil[2] == 0:
                start_position = [x+1, row+1]
                width = height = 0

                for rel_x in range(start_position[0], spritesheet.get_width()):
                    pixil = spritesheet.get_at((rel_x, start_position[1]))
                    if pixil[0] == 255 and pixil[1] == 0 and pixil[2] == 255:
                        width = rel_x - start_position[0]
                        break

                for rel_y in range(start_position[1], spritesheet.get_height()):
                    pixil = spritesheet.get_at((start_position[0], rel_y))
                    if pixil[0] == 255 and pixil[1] == 0 and pixil[2] == 255:
                        height = rel_y - start_position[1]
                        break

                image = pygame.Surface((width, height))
                image.set_colorkey((0,0,0))
                image.blit(spritesheet, (-start_position[0], -start_position[1]))

                images.append(image)

    return images

#Returns the collision between two rects
def rect_rect_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def rect_position_collision(rect, position):
    return (
        position[0] >= rect[0] and
        position[0] < rect[0]+rect[2] and
        position[1] >= rect[1] and
        position[1] < rect[1]+rect[3]
    )

def create_new_animation(animation_data_path, images, loop, scale):
    animation_data = Animation_Data(animation_data_path)
    animation_data.images.clear()
    animation_data.images.extend(images)
    animation_data.config['frames'] = [5 for _ in range(len(images))]
    animation_data.config['loop'] = loop
    animation_data.config['scale'] = scale
    animation = Animation(animation_data)
    return animation

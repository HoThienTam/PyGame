import os
import pygame
import tools
import constants as c

os.environ['SDL_Video_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption(c.ORIGINAL_CAPTION)

SCREEN = pygame.display.set_mode(c.SCREEN_SIZE)

FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))
SFX = tools.load_all_sfx(os.path.join("resources", "sound"))

import setup
from tools import State
import pygame
import constants as c
from components.info import OverheadInfo
from components.mario import Mario


class MainMenu(State):
    def __init__(self):
        State.__init__(self)
        self.image_dict = {}
        self.game_info = {c.COIN_TOTAL: 0,
                          c.SCORE: 0,
                          c.LIVES: 3,
                          c.TOP_SCORE: 0,
                          c.CURRENT_TIME: 0.0,
                          c.LEVEL_STATE: None,
                          c.CAMERA_START_X: 0,
                          c.MARIO_DEAD: False}
        self.overhead_info = OverheadInfo(self.game_info, c.MAIN_MENU)
        self.setup_background()
        self.setup_cursor()
        self.setup_mario()

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = self.get_image(24, 160, 8, 8, setup.GFX['item_objects'])
        self.cursor.rect = (220, 358)
        self.cursor.state = c.PLAYER1

    def setup_mario(self):
        """Places Mario at the beginning of the level"""
        self.mario = Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.GROUND_HEIGHT

    def setup_background(self):
        self.background = setup.GFX['level_1']
        background_rect = self.background.get_rect()

        self.background = pygame.transform.scale(self.background,
                                                 (int(background_rect.width*2.679),
                                                  int(background_rect.height*2.679)))

        self.image_dict['NAME_BOX'] = self.get_image(
            1, 60, 176, 88, setup.GFX['title_screen'])

    def get_image(self, x, y, width, height, sprite):
        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite, (0, 0), (x, y, width, height))
        if sprite == setup.GFX['title_screen']:
            image.set_colorkey((c.HOT_MAGENTA))
            image = pygame.transform.scale(image,
                                           (int(rect.width*2.5),
                                            int(rect.height*2.5)))
        else:
            image.set_colorkey(c.BLACK)
            image = pygame.transform.scale(image,
                                           (int(rect.width*3),
                                            int(rect.height*3)))
        return image

    def update(self, surface, current_time):
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, (0, 0))
        surface.blit(self.image_dict['NAME_BOX'], (170, 100))
        surface.blit(self.cursor.image, self.cursor.rect)
        surface.blit(self.mario.image, self.mario.rect)
        self.overhead_info.draw(surface)

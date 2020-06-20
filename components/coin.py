import pygame
import setup
import constants as c


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = setup.GFX['item_objects']
        self.create_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.first_half = True

    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet"""
        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pygame.transform.scale(image,
                                       (int(rect.width*2.69),
                                        int(rect.height*2.69)))
        return image

    def create_frames(self):
        """Extract coin images from sprite sheet and assign them to a list"""
        self.frames = []
        self.frame_index = 0

        self.frames.append(self.get_image(1, 160, 5, 8))
        self.frames.append(self.get_image(9, 160, 5, 8))
        self.frames.append(self.get_image(17, 160, 5, 8))

    def update(self, current_time):
        """Animates flashing coin"""
        if self.first_half:
            if self.frame_index == 0:
                if (current_time - self.timer) > 375:
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index < 2:
                if (current_time - self.timer) > 125:
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index == 2:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.timer = current_time
        else:
            if self.frame_index == 1:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.timer = current_time

        self.image = self.frames[self.frame_index]

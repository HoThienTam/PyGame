import os
import pygame

keybinding = {
    'action': pygame.K_z,
    'jump': pygame.K_x,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN
}


class Controler:
    def __init__(self, state):
        self.screen = pygame.display.get_surface()
        self.done = False
        self.state = state

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def control(self):
        while not self.done:
            self.event_loop()
            self.current_time = pygame.time.get_ticks()
            self.state.update(self.screen, self.current_time)
            pygame.display.update()


class State:
    def __init__(self):
        self.next = None

    def update(self, surface, current_time):
        pass


def load_all_gfx(directory, colorkey=(255, 0, 255),
                 accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_fonts(directory, accept=('.ttf')):
    return load_all_music(directory, accept)


def load_all_sfx(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pygame.mixer.Sound(os.path.join(directory, fx))
    return effects

import pygame
from load_image import load_image


class LevelChoose():
    def __init__(self, kl):
        self.kl = kl
        self.choose_the_level()

    def choose_the_level(self):
        if self.kl == 1:
            infoObject = pygame.display.Info()
            size = width, height = (infoObject.current_w - 100, infoObject.current_h - 100)
            screen = pygame.display.set_mode(size)
            fon = pygame.transform.scale(load_image('fon1.png'), (width, height))
            screen.blit(fon, (0, 0))
        else:
            pass

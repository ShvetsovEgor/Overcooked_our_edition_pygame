import pygame
from load_image import load_image

allsprites = pygame.sprite.Group()
obstacle = pygame.sprite.Group()


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Floor, self).__init__(allsprites)
        self.image = load_image("cell.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(allsprites, obstacle)
        self.image = load_image("wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

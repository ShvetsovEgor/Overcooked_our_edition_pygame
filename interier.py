import pygame
from load_image import load_image


class Floor(pygame.sprite.Sprite):
    def __init__(self, allsprites,  x, y, cell_size=50):
        super(Floor, self).__init__(allsprites)
        self.image = pygame.transform.scale(load_image("cell.jpg"), (cell_size, cell_size))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, allsprites, obstacle, x, y, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = pygame.transform.scale(load_image("wall.png"), (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

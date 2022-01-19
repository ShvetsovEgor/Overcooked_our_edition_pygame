import pygame
from load_image import load_image


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, cell_size=50):
        super(Floor, self).__init__(allsprites)
        self.image = pygame.transform.scale(load_image("floor.jpg"), (cell_size, cell_size))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = pygame.transform.scale(load_image("wall.jpg"), (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Fridge(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("fridge.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size


class Oven(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("oven.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size


class Knife(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("knife.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size


class Sink(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("sink.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("box.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size


class Table(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, obstacle, cell_size=50):
        super().__init__(allsprites, obstacle)
        self.image = load_image("table.png")
        width, height = self.image.get_rect().size
        k = width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size

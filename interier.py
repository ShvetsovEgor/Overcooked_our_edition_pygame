import pygame
from load_image import load_image
import csv
from food import Ingridients

obstacle = pygame.sprite.Group()
allsprites = pygame.sprite.Group()


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
        print(width, height)
        k = width / cell_size
        print(int(height / k))
        self.image = pygame.transform.scale(self.image, (cell_size, int(height / k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(height / k) + cell_size
        filename = 'level1.csv'
        self.filename = "levels/" + filename
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        num = self.board.index(['---'])
        self.aims = self.board[num + 1:]
        print(self.aims)
        self.board = self.board[:num]
        a = self.aims[-1][0].split()[1:]
        for elem in a:
            print(a)
            Ingridients(self.rect.x, self.rect.y, elem, allsprites)

    def update(self):
        filename = 'level1.csv'
        self.filename = "levels/" + filename
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        num = self.board.index(['---'])
        self.aims = self.board[num + 1:]
        self.board = self.board[:num]
        a = self.aims[-1][0].split()[1:]
        '''
        for elem in a:
            Ingridients(self.rect.x, self.rect.y, elem, allsprites)
        '''
        self.image = load_image("fridge_opened.png")

        width, height = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (150, 200))



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
        self.cell_size = cell_size
        self.width, self.height = self.image.get_rect().size
        self.k = self.width / cell_size
        self.image = pygame.transform.scale(self.image, (cell_size, int(self.height / self.k)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - int(self.height / self.k) + cell_size

        filename = 'level1.csv'
        self.filename = "levels/" + filename
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        num = self.board.index(['---'])
        self.aims = self.board[num + 1:]
        self.board = self.board[:num]
        a = self.aims[-2][0].split()[1:]
        for elem in a:
            Ingridients(self.rect.x, self.rect.y, elem, allsprites)

    def update(self):
        self.image = load_image("box_opened.png")

        self.image = pygame.transform.scale(self.image, (self.cell_size, int(self.height / self.k)))
        '''
        filename = 'level1.csv'
        self.filename = "levels/" + filename
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        num = self.board.index(['---'])
        self.aims = self.board[num + 1:]
        self.board = self.board[:num]
        a = self.aims[-2][0].split()[1:]
        for elem in a:
            Ingridients(self.rect.x, self.rect.y, elem, allsprites)
        '''


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

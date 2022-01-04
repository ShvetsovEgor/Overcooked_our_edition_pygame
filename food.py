import pygame

from load_image import load_image

foodgroup = pygame.sprite.Group()

visual_food = {"Мясо": ["meat.png"],
               'Томат': ['tomato.png'],
               'Нарезанный томат': ['sliced_tomato'],
               "Огурец": ['cucumber.png'],
               "Нарезанный огурец": ['sliced_cucumber'],
               "Картофель": ['tomato.png'],
               "Нарезанный картофель": ['sliced_tomato.png'],
               "Морковь": ['carrot.png'],
               "Нарезанная морковь": ['sliced_carrot.png'],
               'Салат': ['salad.png'],
               'Жареный картофель': ['fried_potato.png']}


# тут будут различные фото для каждой еды [нормальное состояние, нарезанное, сваренное] и т.д.
# надо заполнить

class Food(pygame.sprite.Sprite):
    def __init__(self, title, parent, allsprites, sliced=False, boiled=False, fried=False, shaked=False):
        super().__init__(allsprites, foodgroup)

        self.image = load_image(visual_food[title][0])  # загружаем фото которое соответсвует названию еды
        self.parent = parent  # запоминаем к какому объекту еда прикреплена
        x, y, width, height = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y
        self.rect.w = width + 15
        self.rect.h = height + 15
        # делаем рабочую область чуть больше картинки
        self.title = title
        self.sliced = sliced  # нарезанный
        self.boiled = boiled  # вареный
        self.fried = fried  # жареный
        self.shaked = shaked  # взбитый

    def __eq__(self, other):
        if self.title == other.title and self.sliced == other.sliced and \
                self.boiled == other.boiled and self.fried == other.fried and self.shaked == other.shaked:
            return True
        return False

    def __hash__(self):
        return id(self)


plategroup = pygame.sprite.Group()
FPS = 50
pygame.init()
infoObject = pygame.display.Info()
size = width, height = (infoObject.current_w - 100, infoObject.current_h - 100)
screen = pygame.display.set_mode(size)


class Plate(pygame.sprite.Sprite):
    def __init__(self, allsprites):
        super().__init__(allsprites, plategroup)
        self.image = load_image("red.png")
        self.rect = self.image.get_rect()
        self.clear = True
        self.ingridients = []

    def __eq__(self, other):
        # if set(self.ingridients) == set(other.ingridients):
        #     return True                  требовалось хеширование
        for el in other.ingridients:
            if el not in self.ingridients:
                return False
        if len(self.ingridients) != len(other.ingridients):
            return False
        return True

    def __iadd__(self, other):
        self.ingridients += other
        return self

    def __hash__(self):
        return id(self)


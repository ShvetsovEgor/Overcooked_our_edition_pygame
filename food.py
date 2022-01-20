import pygame

from load_image import load_image

visual_food = {"Название": ["Нормальное состояние", "Нарезанное состояние", "Сваренное состояние", "Жареное состояние"],
               "Мясо": ["meat.png"],
               'Томат': ['tomato.png', 'sliced_tomato.png'],
               "Огурец": ['cucumber.png', 'sliced_cucumber.png'],
               "Картофель": ['tomato.png', 'sliced_tomato.png', 'fried_potato.png'],
               "Морковь": ['carrot.png', 'sliced_carrot.png'],
               'Салат': ['salad.png']}


# тут будут различные фото для каждой еды [нормальное состояние, нарезанное, сваренное] и т.д.
# надо заполнить

class Food(pygame.sprite.Sprite):
    def __init__(self, title, parent, allsprites, foodgroup, sliced=False, boiled=False, fried=False, shaked=False, place=False):
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

    def update(self):
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y

    def change_pic(self, cell_size):
        if self.sliced:
            self.image = pygame.transform.scale(load_image(visual_food[self.title][1]), (cell_size, cell_size))
            x, y, width, height = self.image.get_rect()
            self.rect = self.image.get_rect()
            self.rect.x = self.parent.rect.x
            self.rect.y = self.parent.rect.y


plategroup = pygame.sprite.Group()


class Plate(pygame.sprite.Sprite):
    def __init__(self, parent, allsprites, plategroup, foodgroup, put_able):
        super().__init__(allsprites, plategroup, foodgroup, put_able)
        self.parent = parent
        self.image = pygame.transform.scale(load_image("02_dish_2.png"), (50, 50))
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
        self.ingridients += [other]
        return self

    def __hash__(self):
        return id(self)

    def update(self):
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y
        for el in self.ingridients:
            el.rect.x = self.parent.rect.x
            el.rect.y = self.parent.rect.y



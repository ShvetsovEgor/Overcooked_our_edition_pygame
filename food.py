import pygame

from load_image import load_image

visual_food = {"Название": ["Нормальное состояние", "Нарезанное состояние", "Сваренное состояние", "Жареное состояние"],
               "Мясо": ["meat.png", '', '', '95_steak.png'],
               'Томат': ['tomato.png', 'rounded-texture-tomato.png'],
               "Огурец": ['cucumber.png', 'ronded-texture-cucumber.png'],
               "Картофель": ['potato.png', 'sliced_potato.png', '', 'fried_potato.png'],
               "Морковь": ['carrot.png', 'sliced_carrot.png'],
               "Рыба": ['fish.png', 'sliced_fish.png', '', 'fried_fish.png']
                                   }


# тут будут различные фото для каждой еды [нормальное состояние, нарезанное, сваренное] и т.д.
# надо заполнить

class Food(pygame.sprite.Sprite):
    def __init__(self, title, parent, allsprites, foodgroup, sliced=False, boiled=False, fried=False, shaked=False,
                 place=False):
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

    def __repr__(self):
        return self.title

    def __hash__(self):
        return id(self)

    def update(self):
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y

    def change_pic(self, cell_size):
        if self.sliced:
            self.image = pygame.transform.scale(load_image(visual_food[self.title][1]), (cell_size * 0.8, cell_size * 0.8))
        if self.fried:
            self.image = pygame.transform.scale(load_image(visual_food[self.title][3]), (cell_size * 0.8, cell_size * 0.8))
        x, y, width, height = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y


plategroup = pygame.sprite.Group()


class Plate(pygame.sprite.Sprite):
    def __init__(self, parent, allsprites, plategroup, put_able):
        super().__init__(allsprites, plategroup, put_able)
        self.parent = parent
        self.image = pygame.transform.scale(load_image("02_dish_2.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.clear = True
        self.ingridients = []

    def __eq__(self, other):
        # if set(self.ingridients) == set(other.ingridients):
        #     return True                  #требовалось хеширование
        print("СРАВНЕНИЕ")

        print(other.ingridients, 'other')
        print(self.ingridients, 'self')

        for el in other.ingridients:
            if el not in self.ingridients:
                return False
        if len(self.ingridients) != len(other.ingridients):
            return False
        print('true')
        return True

    def __iadd__(self, other):
        self.ingridients += other
        print(self.ingridients)
        return self

    def __repr__(self):
        line = " ".join([str(x) for x in self.ingridients])
        if line:
            return line
        return "Пустая тарелка"

    def __hash__(self):
        return id(self)

    def update(self):
        self.rect.x = self.parent.rect.x
        self.rect.y = self.parent.rect.y
        for el in self.ingridients:
            el.rect.x = self.parent.rect.x
            el.rect.y = self.parent.rect.y

import pygame.sprite

import food
import interier
from load_image import load_image
from food import Food


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, playersgroup, allsprites, cell_size=50):
        super().__init__(allsprites, playersgroup)
        self.frames = []
        self.dishes = []
        self.cell_size = cell_size
        self.cut_sheet(load_image("walk.png"), 4, 1)
        self.cur_frame = 0
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (cell_size, cell_size))
        self.image = self.frames[self.cur_frame]
        # self.image = load_image("red.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = None
        # предмет в руках
        self.object = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def find(self, foodgroup, put_able):
        # горячие клавиши
        x, y = self.rect.x, self.rect.y
        if not self.object:
            if self.direction == "U":
                self.rect.y -= self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "D":
                self.rect.y += self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "R":
                self.rect.x += self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "L":
                self.rect.x -= self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            print("Берем>", sprite)
            if sprite:
                plates = [x for x in sprite if type(x) == food.Plate]
                if plates:
                    plates[-1].parent = self
                    self.object = plates[-1]
                else:
                    sprite = sprite[-1]
                    sprite.parent = self
                    self.object = sprite
        else:
            if self.direction == "U":
                self.rect.y -= self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "D":
                self.rect.y += self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "R":
                self.rect.x += self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "L":
                self.rect.x -= self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            print("Кладем на", sprites)
            plates = [x for x in sprites if type(x) == food.Plate]

            if plates:
                self.object.image = pygame.transform.scale(self.object.image,
                                                           (plates[-1].image.get_width(),
                                                            plates[-1].image.get_height()))
                self.object.rect = self.object.image.get_rect()
                plates[-1] += [self.object]
                self.object.parent = plates[-1]
                if type(plates[-1]) == interier.Checker:
                    self.object.parent = sprites[-1]
                    plates[-1].check(self.object)
                self.object = False
            elif sprites:
                self.object.parent = sprites[-1]
                if type(sprites[-1]) == interier.Checker:
                    sprites[-1].check(self.object)
                if type(sprites[-1]) == interier.Knife:
                    print(self.object)

                    if type(self.object) == food.Food:
                        self.object.sliced = True
                        self.object.change_pic(self.cell_size)
                self.object = False
                # elif "Table" in str(sprites[-1]) and self.object.sliced:
                #     self.object.place = True
                #     sprite.checkout()
                #     self.object = False

        self.rect.x, self.rect.y = x, y

    def update(self, obstacle, foodgroup=None, plategroup=None):
        go = False
        x = self.rect.x
        y = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.direction = "L"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.x += 5
            else:
                go = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.direction = "R"
            if pygame.sprite.spritecollide(self, obstacle, False):

                self.rect.x -= 5
            else:

                go = True
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            self.direction = "U"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y += 5
            else:
                go = True

        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            self.direction = "D"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y -= 5
            else:
                go = True

        if go:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, playersgroup, allsprites, cell_size=50):
        super().__init__(allsprites, playersgroup)
        self.frames = []
        self.cell_size = cell_size
        self.cut_sheet(load_image("green.png"), 4, 1)
        self.cur_frame = 0
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (cell_size, cell_size))
        self.image = self.frames[self.cur_frame]
        self.image = pygame.transform.scale(load_image("green.png"), (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = None
        # предмет в руках
        self.object = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def find(self, foodgroup, put_able, plategroup):
        # горячие клавиши
        x, y = self.rect.x, self.rect.y
        if not self.object:
            if self.direction == "U":
                self.rect.y -= self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "D":
                self.rect.y += self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "R":
                self.rect.x += self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            elif self.direction == "L":
                self.rect.x -= self.cell_size
                sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            if sprite:
                plates = [x for x in sprite if "Plate" in str(x)]
                if plates:
                    plates[-1].parent = self
                    self.object = plates[-1]
                else:
                    sprite = sprite[-1]
                    sprite.parent = self
                    self.object = sprite
        else:
            if self.direction == "U":
                self.rect.y -= self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "D":
                self.rect.y += self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "R":
                self.rect.x += self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)
            elif self.direction == "L":
                self.rect.x -= self.cell_size
                sprites = pygame.sprite.spritecollide(self, put_able, False)

            if sprites and "Checker" in str(sprites[-1]):
                sprites[-1].check(plates)
                self.object = False

            if sprites and 'Floor' not in str(sprites[-1]) and "Wall" not in str(sprites[-1]):
                # print(sprites)
                print(111)
                plates = [x for x in sprites if "Plate" in str(x)]
                # print(plates)

                if plates:
                    self.object.image = pygame.transform.scale(self.object.image,
                                                               (plates[-1].image.get_width(),
                                                                plates[-1].image.get_height()))
                    self.object.rect = self.object.image.get_rect()
                    plates[-1] += self.object
                    print(plates[-1].ingridients)
                    self.object.parent = plates[-1]
                if "Checker" in str(sprites[-1]):
                    sprites[-1].check(plates)
                    self.object = False

                else:
                    self.object.parent = sprites[-1]
                    if "Knife" in str(sprites[-1]):
                        print(self.object)
                        self.object.sliced = True
                        self.object.change_pic(self.cell_size)

        self.rect.x, self.rect.y = x, y

    def update(self, obstacle, foodgroup=None, plategroup=None):
        go = False
        x = self.rect.x
        y = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            self.direction = "L"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.x += 5
            else:
                go = True

        if keys[pygame.K_d]:
            self.rect.x += 5
            self.direction = "R"
            if pygame.sprite.spritecollide(self, obstacle, False):

                self.rect.x -= 5
            else:

                go = True
        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.direction = "U"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y += 5
            else:
                go = True

        if keys[pygame.K_s]:
            self.rect.y += 5
            self.direction = "D"
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y -= 5
            else:
                go = True

        # if go:
        #     self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        #     self.image = self.frames[self.cur_frame]

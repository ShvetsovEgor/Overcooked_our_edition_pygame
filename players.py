import pygame.sprite
from load_image import load_image
from food import Food


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, playersgroup, allsprites, cell_size=50):
        super().__init__(allsprites, playersgroup)
        self.frames = []
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
        self.object = None

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def find(self, foodgroup):
        if self.direction == "U":
            self.rect.y -= 20
            sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            print(sprite)
            if sprite is not None:
                sprite = sprite[-1]
                sprite.parent = self
            # print("Текущий объект", sprite.title)
            self.rect.y += 20
            return (1, sprite)

        elif self.direction == "D":
            self.rect.y += 20
            sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            if sprite is not None:
                sprite = sprite[0]
                sprite.parent = self
            # print("Текущий объект", sprite.title)
            self.rect.y -= 20
            return (1, sprite)

        elif self.direction == "R":
            self.rect.x -= 20
            sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            if sprite is not None:
                sprite = sprite[0]
                sprite.parent = self
            # print("Текущий объект", sprite.title)
            self.rect.x += 20
            return (1, sprite)

        elif self.direction == "L":
            self.rect.x -= 20
            sprite = pygame.sprite.spritecollide(self, foodgroup, False)
            if sprite is not None:
                sprite = sprite[0]
                sprite.parent = self
            # print("Текущий объект", sprite.title)
            self.rect.x += 20
            return (1, sprite)

    def put(self, obstacle, sprite_now):

        if self.direction == "U":
            self.rect.y -= 20
            sprite = pygame.sprite.spritecollide(self, obstacle, False)
            # print(sprite)
            if sprite is not None and 'Floor' not in str(sprite) and "Wall" not in str(sprite):
                sprite = sprite[-1]
                sprite_now.parent = sprite
                if "Knife" in str(sprite):
                    print(sprite_now)

                    sprite_now.sliced = True
                    sprite_now.change_pic()
            # print("Текущий объект", sprite)
            self.rect.y += 20
            print(sprite_now.sliced)
            return 1

        elif self.direction == "D":
            self.rect.y += 20
            sprite = pygame.sprite.spritecollide(self, obstacle, False)
            if sprite and 'Floor' not in str(sprite) and "Wall" not in str(sprite):
                sprite = sprite[0]
                sprite_now.parent = sprite
            # print("Текущий объект", sprite)
            self.rect.y -= 20
            if "Knife" in str(sprite):
                print(sprite_now)

                sprite_now.sliced = True
                sprite_now.change_pic()
            return 1

        elif self.direction == "R":
            self.rect.x -= 20
            sprite = pygame.sprite.spritecollide(self, obstacle, False)
            if sprite and 'Floor' not in str(sprite) and "Wall" not in str(sprite):
                sprite = sprite[0]
                sprite_now.parent = sprite
            # print("Текущий объект", sprite)
            self.rect.x += 20
            if "Knife" in str(sprite):
                print(sprite_now)

                sprite_now.sliced = True
                sprite_now.change_pic()
            return 1

        elif self.direction == "L":
            self.rect.x -= 20
            sprite = pygame.sprite.spritecollide(self, obstacle, False)
            if sprite and 'Floor' not in str(sprite) and "Wall" not in str(sprite):
                sprite = sprite[0]
                sprite_now.parent = sprite

            # print("Текущий объект", sprite)
            self.rect.x += 20
            if "Knife" in str(sprite):
                print(sprite_now)

                sprite_now.sliced = True
                sprite_now.change_pic()
            return 1

    def update(self, obstacle, foodgroup=None, plategroup=None, ):

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
        # self.frames = []
        # self.cut_sheet(load_image("walk.png"), 4, 1)
        # self.cur_frame = 0
        # for i in range(len(self.frames)):
        #     self.frames[i] = pygame.transform.scale(self.frames[i], (cell_size, cell_size))
        # self.image = self.frames[self.cur_frame]
        self.image = load_image("green.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.object = None

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, obstacle):
        go = False
        x = self.rect.x
        y = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y += 5
            else:
                go = True

        if keys[pygame.K_d]:
            self.rect.x += 5
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.x -= 5
            else:
                go = True
        if keys[pygame.K_w]:
            self.rect.y -= 5
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y += 5
            else:
                go = True

        if keys[pygame.K_s]:
            self.rect.y += 5
            if pygame.sprite.spritecollide(self, obstacle, False):
                self.rect.y -= 5
            else:
                go = True

        # if go:
        #     self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        #     self.image = self.frames[self.cur_frame]

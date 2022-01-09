import pygame.sprite
from load_image import load_image


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

    def update(self, obstacle, foodgroup=None, plategroup=None, event=None):
        if event is not None:
            sprite = pygame.sprite.spritecollideany(self, foodgroup)
            if event.button == pygame.K_m and sprite:
                self.object = sprite
                sprite.parent = self
        else:
            go = False
            x = self.rect.x
            y = self.rect.y
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                if pygame.sprite.spritecollide(self, obstacle, False):
                    s = str(pygame.sprite.spritecollide(self, obstacle, False)).split()[0][2:]
                    print(s)
                    self.rect.x += 5
                else:
                    go = True

            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                if pygame.sprite.spritecollide(self, obstacle, False):
                    s = str(pygame.sprite.spritecollide(self, obstacle, False)).split()[0][2:]
                    print(s)
                    print("Столкновение")
                    self.rect.x -= 5
                else:
                    go = True
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                if pygame.sprite.spritecollide(self, obstacle, False):
                    s = str(pygame.sprite.spritecollide(self, obstacle, False)).split()[0][2:]
                    print(s)
                    self.rect.y += 5
                else:
                    go = True

            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                if pygame.sprite.spritecollide(self, obstacle, False):
                    s = str(pygame.sprite.spritecollide(self, obstacle, False)).split()[0][2:]
                    print(s)
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

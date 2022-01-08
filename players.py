import pygame.sprite
from load_image import load_image
from interier import Wall
playersgroup = pygame.sprite.Group()
obstacle = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites, cell_size, board):
        super().__init__(allsprites, playersgroup)
        self.frames = []
        self.board = board
        self.cut_sheet(load_image("walk.png"), 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.image = load_image("red.png")
        self.rect = self.image.get_rect()
        self.cell_size = cell_size
        self.image = pygame.transform.scale(self.image, (self.cell_size, self.cell_size))
        self.rect.x = x
        self.rect.y = y

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def get_type(self, x, y):
        self.x1 = x - 100
        self.y1 = y - 300
        self.x1 //= self.cell_size
        self.y1 //= self.cell_size
        print(self.x1, self.y1)
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == '.':
                    pass
                elif self.board[x][y] == '#':
                    t = Wall(y * self.cell_size + 300, x * self.cell_size + 100, self.cell_size)
                    obstacle.add(t)
                elif self.board[x][y] == '@':
                    pass



    def update(self):
        go = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if pygame.sprite.spritecollideany(self, obstacle):
                self.rect.x += 5
            go = True

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.get_type(self.rect.x, self.rect.y)
            if pygame.sprite.spritecollideany(self, obstacle):
                self.rect.x -= 5
            go = True

        if keys[pygame.K_UP]:
            self.rect.y -= 5
            if pygame.sprite.spritecollideany(self, obstacle):
                self.rect.y += 5
            go = True

        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            if pygame.sprite.spritecollideany(self, obstacle):
                self.rect.y -= 5
            go = True


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites):
        super().__init__(allsprites, playersgroup, cell_size)
        self.image = load_image("green.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5

        if keys[pygame.K_d]:
            self.rect.x += 5

        if keys[pygame.K_w]:
            self.rect.y -= 5

        if keys[pygame.K_s]:
            self.rect.y += 5


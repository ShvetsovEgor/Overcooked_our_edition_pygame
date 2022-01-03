import pygame.sprite
from load_image import load_image

playersgroup = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites):
        super().__init__(allsprites, playersgroup)
        self.image = load_image("red.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1

        if keys[pygame.K_RIGHT]:
            self.rect.x += 1

        if keys[pygame.K_UP]:
            self.rect.y -= 1

        if keys[pygame.K_DOWN]:
            self.rect.y += 1


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, allsprites):
        super().__init__(allsprites, playersgroup)
        self.image = load_image("green.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 1

        if keys[pygame.K_d]:
            self.rect.x += 1

        if keys[pygame.K_w]:
            self.rect.y -= 1

        if keys[pygame.K_s]:
            self.rect.y += 1

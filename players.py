import pygame.sprite
from load_image import load_image

players = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(players)
        self.image = load_image("")
        self.rect = self.image.get_rect()

    def update(self, event):
        if event.key == pygame.K_UP:
            self.rect.y -= 10
        if event.key == pygame.K_DOWN:
            self.rect.y += 10
        if event.key == pygame.K_LEFT:
            self.rect.x -= 10
        if event.key == pygame.K_RIGHT:
            self.rect.x += 10


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(players)
        self.image = load_image("")
        self.rect = self.image.get_rect()

    def update(self, event):
        if event.key == pygame.K_w:
            self.rect.y -= 10
        if event.key == pygame.K_s:
            self.rect.y += 10
        if event.key == pygame.K_a:
            self.rect.x -= 10
        if event.key == pygame.K_d:
            self.rect.x += 10


class Level(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()
        surf = pygame.Surface([40, 40])
        pygame.draw.rect(surf, "green", x, y)
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(str(number), 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        surf.blit(string_rendered, intro_rect)


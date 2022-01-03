import pygame
from players import playersgroup
platformgroup = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, text, color):
        super().__init__(platformgroup)
        self.text = text
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color(color))

        intro_rect = string_rendered.get_rect()
        pygame.draw.rect(string_rendered, color, intro_rect, width=5)

        intro_rect.y = y
        intro_rect.x = x
        self.rect = intro_rect
        screen.blit(string_rendered, intro_rect)

    def update(self, event):
        if pygame.sprite.groupcollide(playersgroup, platformgroup, False, False):
            print("Загрузка уровня")

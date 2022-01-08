import pygame
from load_image import load_image


class LevelPlatform(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, platformgroup, allsprites, text, color):
        super().__init__(allsprites, platformgroup)
        self.text = text
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color(color))
        self.image = load_image("platform.png")
        self.rect = string_rendered.get_rect()
        self.image.blit(string_rendered, self.rect)
        pygame.draw.rect(self.image, color, self.rect, width=5)
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)

    def update(self, playersgroup):
        info = pygame.sprite.spritecollide(self, playersgroup, False)
        if len(info) == len(playersgroup) != 0:
            return self.text

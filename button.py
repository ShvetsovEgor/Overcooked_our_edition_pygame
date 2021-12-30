import pygame

ButtonGroup = pygame.sprite.Group()


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, text, y, x):
        super().__init__(*ButtonGroup)
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()

        intro_rect.y = y
        intro_rect.x = x
        self.rect = intro_rect
        screen.blit(string_rendered, intro_rect)
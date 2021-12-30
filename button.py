import pygame

ButtonGroup = pygame.sprite.Group()


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, text):
        super().__init__(*ButtonGroup)
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = x
        intro_rect.x = y
        self.rect = intro_rect
        screen.blit(string_rendered, intro_rect)

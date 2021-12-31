import pygame

buttongroup = pygame.sprite.Group()


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, text):
        super().__init__(buttongroup)
        self.text = text
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(text, 1, pygame.Color('white'))

        intro_rect = string_rendered.get_rect()
        pygame.draw.rect(string_rendered, "white", intro_rect, width=5)

        intro_rect.y = y
        intro_rect.x = x
        self.rect = intro_rect
        screen.blit(string_rendered, intro_rect)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(event.pos):
            print(self.text)

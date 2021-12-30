import pygame

from load_image import load_image
from button import Button, ButtonGroup

FPS = 50
pygame.init()
infoObject = pygame.display.Info()
size = width, height = (infoObject.current_w - 100, infoObject.current_h - 100)
screen = pygame.display.set_mode(size)


class HelloScene:  # После нажатия любой клавиши должен появится красный экран с двумя кнопками 1 игрока или два
    # при нажатии на одну из этих кнопок, загружается поле с уровнями, и в цикле проверяется находятся ли все игроки в
    # пересечении со спрайтом плитки уровня
    def __init__(self):
        running = True
        self.fon()
        self.text()
        while running:
            FPS = 100
            clock = pygame.time.Clock()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    one = Button(screen, "1P", 100, 100)
                    two = Button(screen, "2P", 100, 200)
                if event.type == pygame.MOUSEBUTTONDOWN and \
                        one.rect.collidepoint(event.pos):
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN and \
                        two.rect.collidepoint(event.pos):
                    pass

            clock.tick(FPS)
            pygame.display.flip()

    def fon(self):
        fon = pygame.transform.scale(load_image('fon.png'), (width, height))
        screen.blit(fon, (0, 0))

    def text(self):
        font = pygame.font.Font(None, 100)
        string_rendered = font.render("Overcooked", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = 70
        intro_rect.x = 70
        screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 70)
        string_rendered = font.render("Tap any button to start", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = height - 100
        intro_rect.x = 0
        screen.blit(string_rendered, intro_rect)


if __name__ == '__main__':
    pygame.display.set_caption("Заготовки")
    scene = HelloScene()

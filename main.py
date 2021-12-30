import pygame
from load_image import load_image

FPS = 50
pygame.init()
infoObject = pygame.display.Info()
size = width, height = (infoObject.current_w, infoObject.current_h)
screen = pygame.display.set_mode(size)


class HelloScene:
    def __init__(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            screen.fill((0, 0, 255))
            self.fon()
            self.text()
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


if __name__ == '__main__':
    pygame.display.set_caption("Заготовки")


    # создадим спрайт

    # добавим спрайт в группу
    scene = HelloScene()


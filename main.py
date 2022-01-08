import pygame

from load_image import load_image
from button import Button
from levelchoose import LevelChoose

FPS = 50
pygame.init()
infoObject = pygame.display.Info()
size = width, height = (infoObject.current_w - 100, infoObject.current_h - 100)
screen = pygame.display.set_mode(size)


class HelloScene:  # После нажатия любой клавиши должен появится красный экран с двумя кнопками 1 игрока или два
    # при нажатии на одну из этих кнопок, загружается поле с уровнями, и в цикле проверяется находятся ли все игроки в
    # пересечении со спрайтом плитки уровня
    def __init__(self, width, height):
        self.buttongroup = pygame.sprite.Group()

        FPS = 100
        running = True
        self.width = width
        self.height = height
        self.fon()
        self.text()
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    screen.fill("red")
                    Button(screen, width // 2 - 200, height // 2, self.buttongroup, "1P", "white")
                    Button(screen, width // 2 + 200, height // 2,self.buttongroup,  "2P", "white")
                for el in self.buttongroup:
                    reaction = el.update(event)
                    if reaction == "1P":
                        running = False
                        LevelChoose(self, screen, 1)
                    elif reaction == "2P":
                        running = False
                        LevelChoose(self, screen, 2)

            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

    def fon(self):
        fon = pygame.transform.scale(load_image('fon.png'), (width, height))
        screen.blit(fon, (0, 0))

    def text(self):
        # font = pygame.font.Font(None, 100)
        # string_rendered = font.render("Overcooked", 1, pygame.Color('white'))
        # intro_rect = string_rendered.get_rect()
        # intro_rect.y = 70
        # intro_rect.x = 70
        # screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 70)
        string_rendered = font.render("Tap any button to start", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.y = height - 100
        intro_rect.x = 0

        screen.blit(string_rendered, intro_rect)


if __name__ == '__main__':
    pygame.display.set_caption("")
    scene = HelloScene(width, height)

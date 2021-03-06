import pygame
from pygame import mixer
from button import Button
from levelchoose import LevelChoose
from load_image import load_image
FULLSCREEN = True
FPS = 50
pygame.init()
infoObject = pygame.display.Info()
if FULLSCREEN:
    size = width, height = (infoObject.current_w, infoObject.current_h)
else:
    size = width, height = (infoObject.current_w - 50, infoObject.current_h - 50)
screen = pygame.display.set_mode(size)


class HelloScene:  # После нажатия любой клавиши должен появится красный экран с двумя кнопками 1 игрока или два
    # при нажатии на одну из этих кнопок, загружается поле с уровнями, и в цикле проверяется находятся ли все игроки в
    # пересечении со спрайтом плитки уровня
    def __init__(self, width, height):
        self.buttongroup = pygame.sprite.Group()
        self.button_sound = mixer.Sound('sounds/button.mp3')
        mixer.music.load('sounds/main_music.mp3')
        mixer.music.play()
        FPS = 100
        self.running = True
        self.width = width
        self.height = height
        self.fon()
        self.text()
        clock = pygame.time.Clock()
        while self.running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                        else:
                            screen.fill("red")
                            Button(screen, width // 2 - 200, height // 2, self.buttongroup, "1P", "white")
                            Button(screen, width // 2 + 200, height // 2, self.buttongroup, "2P", "white")
                    for el in self.buttongroup:
                        reaction = el.update(event)
                        if reaction == "1P":
                            self.button_sound.play()
                            mixer.music.set_volume(0.5)
                            LevelChoose(self, screen, 1)

                            self.running = False
                        elif reaction == "2P":
                            self.button_sound.play()
                            mixer.music.set_volume(0.5)
                            LevelChoose(self, screen, 2)

                            self.running = False

                    clock.tick(FPS)
                    pygame.display.flip()
            except Exception:
                print("Завершение работы приложения")
                pygame.quit()
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
    pygame.display.set_caption("Overcooked - our edition")
    scene = HelloScene(width, height)

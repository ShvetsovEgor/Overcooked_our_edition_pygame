import sqlite3

import pygame
from pygame import mixer
from gameplay import GamePlayScene
from level_platform import LevelPlatform
from level_platform import Road
from players import Player, SecondPlayer


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, width, height):
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.height // 2)


class LevelChoose:
    def __init__(self, parent, screen, kl):
        self.playersgroup = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.platformgroup = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.screen = screen
        self.button_sound = mixer.Sound('sounds/button.mp3')
        self.kol = kl
        con = sqlite3.connect("level_history.db")
        cur = con.cursor()
        result = cur.execute("Select * from history").fetchall()
        x = 0
        y = self.parent.height // 2

        if self.kol == 1:
            self.obj = Player(50, y - 50, self.playersgroup, self.allsprites, self)
        else:
            self.obj = Player(50, y - 70, self.playersgroup, self.allsprites, self)
            SecondPlayer(50, y - 20, self.playersgroup, self.allsprites, self)

        pygame.draw.rect(self.screen, "black", (0, y - 100, x, 200))

        # запрос из БД!
        print(result)
        y -= 100
        Road(x, y - 10, self.allsprites)
        x += 150
        for el in result:
            Road(x, y - 10, self.allsprites)
            Road(x + 150, y - 10, self.allsprites)
            if el[1]:
                LevelPlatform(self.screen, x, y, self.platformgroup, self.allsprites, str(el[0]), "green")
            else:
                LevelPlatform(self.screen, x, y, self.platformgroup, self.allsprites, str(el[0]), "red")
            x += 300
        self.choose_the_level()

    def choose_the_level(self):
        FPS = 30
        self.running = True
        clock = pygame.time.Clock()
        camera = Camera(self.parent.width, self.parent.height)
        while self.running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.parent.running = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.running = False
                        self.parent.running = False

                self.screen.fill((0, 0, 255))

                camera.update(self.obj)
                for el in self.allsprites:
                    camera.apply(el)
                self.allsprites.draw(self.screen)
                self.playersgroup.update(self.obstacle)

                for el in self.platformgroup:
                    level_number = el.update(self.playersgroup)
                    if level_number is not None:
                        GamePlayScene(self, level_number, self.screen)
                        mixer.music.load('sounds/main_music.mp3')
                        mixer.music.play()
                        if self.kol == 2:
                            LevelChoose(self, self.screen, 2)
                        else:
                            LevelChoose(self, self.screen, 1)
                self.platformgroup.draw(self.screen)
                self.playersgroup.draw(self.screen)
                pygame.display.flip()
                clock.tick(FPS)
            except Exception as e:
                self.running = False
                print(e)
                print("Выход из цикла выбора уровня")
                pygame.quit()
        pygame.quit()

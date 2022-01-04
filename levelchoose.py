import sqlite3
import pygame
from load_image import load_image
from players import playersgroup, Player, SecondPlayer
from level_platform import LevelPlatform, platformgroup
from gameplay import GamePlayScene
allsprites = pygame.sprite.Group()


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
        self.parent = parent
        self.screen = screen
        self.kol = kl

        fon = pygame.transform.scale(load_image('fon1.png'), (self.parent.width, self.parent.height))
        self.screen.blit(fon, (0, 0))
        con = sqlite3.connect("level_history.db")
        cur = con.cursor()
        result = cur.execute("Select * from history").fetchall()
        x = 200
        y = self.parent.height // 2

        if self.kol == 1:
            self.obj = Player(50, y - 50, allsprites)
        else:
            self.obj = Player(50, y - 50, allsprites)
            SecondPlayer(50, y + 50, allsprites)

        pygame.draw.rect(self.screen, "black", (0, y - 100, x, 200))

        # запрос из БД!
        print(result)
        y -= 100
        for el in result:
            # рисуем мостик или дорогу
            if el[1]:
                LevelPlatform(self.screen, x, y, str(el[0]), "green", allsprites)
            else:
                LevelPlatform(self.screen, x, y, str(el[0]), "red", allsprites)
            x += 300
        self.choose_the_level()

    def choose_the_level(self):
        FPS = 30
        running = True
        clock = pygame.time.Clock()
        camera = Camera(self.parent.width, self.parent.height)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((0, 0, 255))
            camera.update(self.obj)
            for el in allsprites:
                camera.apply(el)
            playersgroup.update()
            for el in platformgroup:
                level_number = el.update()
                if level_number is not None:
                    print(level_number)
                    GamePlayScene(self, "level" + level_number + ".csv", self.screen)
            platformgroup.draw(self.screen)
            playersgroup.draw(self.screen)
            pygame.display.flip()
            clock.tick(FPS)
            # pygame.event.pump()
        pygame.quit()

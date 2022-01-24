import csv
import datetime
import sqlite3
from random import choice

import pygame.sprite
from pygame import mixer

from dishes import *
from interier import Floor, Wall, Fridge, Oven, Knife, Sink, Box, Table, Checker
from players import Player, SecondPlayer


class GamePlayScene:
    def __init__(self, parent, filenumber, screen):
        self.obstacle = pygame.sprite.Group()
        self.playersgroup = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.foodgroup = pygame.sprite.Group()
        self.plategroup = pygame.sprite.Group()
        self.put_able = pygame.sprite.Group()
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.screen = screen
        self.filename = f"levels/level{filenumber}.csv"
        self.filenumber = filenumber
        self.first_time = datetime.datetime.now()
        self.result = {}
        self.load_level()
        self.running = True
        mixer.music.load('sounds/gameplay.mp3')
        mixer.music.play()
        FPS = 60
        clock = pygame.time.Clock()
        countdown = True
        while self.running:
            # try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.parent.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.first_player.find(self.foodgroup, self.put_able)
                    elif event.key == pygame.K_e:
                        self.second_player.find(self.foodgroup, self.put_able)

            font = pygame.font.Font(None, 50)
            if countdown and datetime.datetime.now() - self.first_time > datetime.timedelta(seconds=self.time - 11):
                countdown = False
                mixer.music.load('sounds/countdown.mp3')
                mixer.music.play()
            if datetime.datetime.now() - self.first_time > datetime.timedelta(seconds=self.time):
                self.show_result()
            else:
                text = font.render(
                    str(self.first_time + datetime.timedelta(seconds=self.time) - datetime.datetime.now()), True,
                    (100, 255, 100))

            self.screen.fill("white")

            self.allsprites.draw(self.screen)
            self.plategroup.update()
            self.plategroup.draw(self.screen)

            self.foodgroup.update()
            self.foodgroup.draw(self.screen)

            self.playersgroup.update(self.obstacle)
            self.playersgroup.draw(self.screen)
            lines = []
            for el in self.titles:
                lines += [el + ":"]
                lines += str(globals()[el]).split()
            for i, el in enumerate(lines):
                screen.blit(font.render(el, True, (100, 255, 100)),
                            (self.width - self.border_x, 100 + 50 * i))

            screen.blit(text, (self.width - self.border_x, 50))  # таймер
            clock.tick(FPS)
            pygame.display.flip()
        # except Exception as e:
        #     self.running = False
        #     print(e)
        #     print("Выход из цикла игры")

    def load_level(self):
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        self.cell_size = min(self.width // len(self.board[0]), self.height // len(self.board))
        self.border_x = (self.width - self.cell_size * len(self.board[0])) // 2
        self.border_y = (self.height - self.cell_size * len(self.board)) // 2
        con = sqlite3.connect('level_history.db')
        cur = con.cursor()
        res = cur.execute(f"SELECT * FROM history WHERE level_id = {int(self.filenumber)}").fetchone()
        self.time = res[5]
        self.title = res[2]
        self.dishes = []
        self.titles = []
        for el in res[3].split(", "):
            self.dishes += [globals()[el]]
            self.titles += [el]
            print(self.dishes)

        self.ingridients = {}
        for el in res[4].split("; "):
            el = el.split(": ")

            if el[0] in self.ingridients:
                self.ingridients[el[0]] += el[1].split(", ")
            else:
                self.ingridients[el[0]] = el[1].split(", ")
        print(self.ingridients)
        self.generate_level()

    def generate_level(self):
        floors = []
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                vect_x, vect_y = self.border_x + x * self.cell_size, self.border_y + y * self.cell_size
                if self.board[y][x] == '.':
                    Floor(vect_x, vect_y, self.allsprites, self.cell_size)
                    floors += [(vect_x, vect_y)]
                elif self.board[y][x][0] == '#':
                    Wall(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x][0] == 'f':
                    parent = Fridge(vect_x, vect_y, self.allsprites, self.obstacle, self.put_able, self.cell_size)
                    for title in self.ingridients["Fridge"]:
                        f = Food(title, parent, self.allsprites, self.foodgroup)
                        f.image = pygame.transform.scale(f.image, (self.cell_size, self.cell_size))
                elif self.board[y][x][0] == 'o':
                    Oven(vect_x, vect_y, self.allsprites, self.obstacle, self.put_able, self.cell_size)
                elif self.board[y][x][0] == 'k':
                    Knife(vect_x, vect_y, self.allsprites, self.obstacle, self.put_able, self.cell_size)
                elif self.board[y][x][0] == 's':
                    Sink(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x][0] == 'b':
                    parent = Box(vect_x, vect_y, self.allsprites, self.obstacle, self.put_able, self.cell_size)
                    for title in self.ingridients["Box"]:
                        f = Food(title, parent, self.allsprites, self.foodgroup)
                        f.image = pygame.transform.scale(f.image, (self.cell_size, self.cell_size))
                elif self.board[y][x][0] == 't':
                    t = Table(vect_x, vect_y, self.allsprites, self.obstacle, self.put_able, self.cell_size)
                    if len(self.board[y][x]) == 2 and self.board[y][x][1] == "p":
                        Plate(t, self.allsprites, self.plategroup, self.foodgroup, self.put_able)
                elif self.board[y][x][0] == 'c':
                    self.checker = Checker(vect_x, vect_y, self.allsprites, self, self.obstacle, self.put_able,
                                           self.cell_size)
                # Декодировка символов в классы

        self.rows = x
        self.cols = y

        if self.parent.kol == 2:
            x, y = choice(floors)
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size - 5)
            self.first_player.dishes = self.dishes
            self.second_player = SecondPlayer(x, y, self.playersgroup, self.allsprites, self.cell_size - 5)
        elif self.parent.kol == 1:
            x, y = choice(floors)
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size - 5)

    def show_result(self):
        self.running = False
        # pygame.quit()
        # self.running = False
        # FPS = 50
        # pygame.init()
        # infoObject = pygame.display.Info()
        # size = width, height = (infoObject.current_w - 50, infoObject.current_h - 50)
        # screen = pygame.display.set_mode(size)
        # screen.fill(pygame.Color('white'))
        cnt, mx = len([x for x in self.result.values() if x]), len(self.result.values())
        print(f"result {cnt} of {mx}")
        if cnt == mx:
            con = sqlite3.connect('level_history.db')
            cur = con.cursor()
            cur.execute(f"UPDATE history SET status = 1 WHERE level_id = {int(self.filenumber)}")
            con.commit()
            con.close()
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    running = False
            pygame.display.flip()

            pygame.draw.rect(self.screen, "red", (0, 0, width, height))
            font = pygame.font.Font(None, 60)
            string_rendered = font.render(f"Поздравляем, ваш результат {cnt}/{mx}", 1,
                                          pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            intro_rect.y = self.border_y + 200
            intro_rect.x = self.border_x
            self.screen.blit(string_rendered, intro_rect)
            clock.tick(60)

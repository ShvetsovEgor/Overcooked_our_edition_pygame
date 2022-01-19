import csv
import sqlite3
import pygame.sprite
from random import choice
from interier import Floor, Wall, Fridge, Oven, Knife, Sink, Box, Table
from players import Player, SecondPlayer
from dishes import *
import datetime

infoObject = pygame.display.Info()
size = width, height = (infoObject.current_w - 50, infoObject.current_h - 50)


class GamePlayScene:
    def __init__(self, parent, filenumber, screen):
        self.obstacle = pygame.sprite.Group()
        self.playersgroup = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.foodgroup = pygame.sprite.Group()
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.screen = screen
        self.filename = f"levels/level{filenumber}.csv"
        self.filenumber = filenumber
        self.f1 = 0
        self.f2 = 0
        self.first_time = datetime.datetime.now()

        self.load_level()
        self.running = True
        FPS = 60
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.parent.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(self.f1)  # горячие клавиши
                        if not self.f1:

                            self.f1 = 1
                            self.sprite = self.first_player.find(self.foodgroup)[1]

                        elif self.f1 == 1:
                            self.first_player.put(self.obstacle, self.sprite)
                            self.f1 = 0
                            self.sprite = None

                    elif event.key == pygame.K_e:
                        self.second_player.find(self.foodgroup)
            if self.running:
                font = pygame.font.Font(None, 50)
                text = font.render(str(datetime.datetime.now() - self.first_time), True, (100, 255, 100))

                self.screen.fill("white")

                self.allsprites.draw(self.screen)
                self.obstacle.draw(self.screen)
                self.foodgroup.draw(self.screen)

                self.playersgroup.draw(self.screen)
                self.playersgroup.update(self.obstacle)
                self.foodgroup.update()
                screen.blit(text, (width - 300, 50))
                clock.tick(FPS)
                pygame.display.flip()
        pygame.quit()

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
        self.title = res[2]
        self.dishes = []
        for el in res[3].split(", "):
            self.dishes += [globals()[el]]
        self.ingridients = {}
        for el in res[4].split(";"):
            el = el.split(": ")

            if el[0] in self.ingridients:
                self.ingridients[el[0]] += el[1].split(", ")
            else:
                self.ingridients[el[0]] = el[1].split(", ")

        self.generate_level()

    def generate_level(self):
        floors = []
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                vect_x, vect_y = self.border_x + x * self.cell_size, self.border_y + y * self.cell_size
                if self.board[y][x] == '.':
                    Floor(vect_x, vect_y, self.allsprites, self.cell_size)
                    floors += [(vect_x, vect_y)]
                elif self.board[y][x] == '#':
                    Wall(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x] == 'f':
                    Fridge(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x] == 'o':
                    Oven(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x] == 'k':
                    Knife(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x] == 's':
                    Sink(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                elif self.board[y][x] == 'b':
                    parent = Box(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                    for title in self.ingridients["Box"]:
                        f = Food(title, parent, self.allsprites, self.foodgroup)
                        f.image = pygame.transform.scale(f.image, (self.cell_size, self.cell_size))


                elif self.board[y][x] == 't':
                    Table(vect_x, vect_y, self.allsprites, self.obstacle, self.cell_size)
                # Декодировка символов в классы

        self.rows = x
        self.cols = y

        if self.parent.kol == 2:
            x, y = choice(floors)  # вопрос
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size)
            self.second_player = SecondPlayer(x, y, self.playersgroup, self.allsprites)
        elif self.parent.kol == 1:
            x, y = choice(floors)   # вопрос
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size - 5)
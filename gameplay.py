import csv
from food import Food
from interier import Floor, Wall
import pygame.sprite

from players import Player, SecondPlayer


class GamePlayScene:
    def __init__(self, parent, filename, screen):
        self.allsprites = pygame.sprite.Group()
        self.playersgroup = pygame.sprite.Group()

        self.foodgroup = pygame.sprite.Group()
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.screen = screen
        self.cell_size = 100
        self.filename = "levels/" + filename
        # for el in allsprites:
        #     el.kill()
        # for el in platformgroup:
        #     el.kill()
        # for el in playersgroup:
        #     el.kill()
        self.load_level()
        running = True
        FPS = 60

        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill("green")

            self.allsprites.draw(self.screen)
            self.allsprites.update()
            self.playersgroup.draw(self.screen)
            # self.first_player.update()
            self.playersgroup.update()
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
        self.generate_level()

    def generate_level(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                vect_x, vect_y = self.border_x + x * self.cell_size, self.border_y + y * self.cell_size
                if self.board[y][x] == '.':
                    Floor(vect_x, vect_y, self.cell_size)
                elif self.board[y][x] == '#':
                    Wall(self.allsprites, self.obstacle, vect_x, vect_y, self.cell_size)
                elif self.board[y][x] == '@':
                    s = Floor(vect_x, vect_y, self.cell_size)
                    meat = Food("Мясо", s, self.allsprites, self.foodgroup)
                # Декодировка символов в классы

        self.rows = x
        self.cols = y

        if self.parent.kol == 2:
            x, y = 0, 0  # вопрос
            allsprites = pygame.sprite.Group()
            self.first_player = Player(x, y, allsprites, self.cell_size)
            self.second_player = SecondPlayer(x, y, allsprites, self.cell_size)
        elif self.parent.kol == 1:
            x, y = 100, 100  # вопрос
            allsprites = pygame.sprite.Group()
            self.first_player = Player(x, y, allsprites, self.cell_size)

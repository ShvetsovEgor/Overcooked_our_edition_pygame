import csv
import pygame.sprite
from interier import Floor, Wall
from players import Player, SecondPlayer


class GamePlayScene:
    def __init__(self, parent, filename, screen):
        self.obstacle = pygame.sprite.Group()
        self.playersgroup = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.foodgroup = pygame.sprite.Group()
        self.parent = parent
        self.width = self.parent.width
        self.height = self.parent.height
        self.screen = screen
        self.filename = "levels/" + filename

        self.load_level()
        running = True
        FPS = 60
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.playersgroup.take(event, self.foodgroup)
            self.screen.fill("green")

            self.allsprites.draw(self.screen)
            self.playersgroup.draw(self.screen)
            self.playersgroup.update(self.obstacle)
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
                    Floor(vect_x, vect_y, self.allsprites, self.cell_size)
                elif self.board[y][x] == '#':
                    Wall(vect_x, vect_y, self.allsprites, self.obstacle,  self.cell_size)
                # Декодировка символов в классы

        self.rows = x
        self.cols = y

        if self.parent.kol == 2:
            x, y = 0, 0  # вопрос
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size)
            self.second_player = SecondPlayer(x, y, self.playersgroup, self.allsprites)
        elif self.parent.kol == 1:
            x, y = 100, 100  # вопрос
            self.first_player = Player(x, y, self.playersgroup, self.allsprites, self.cell_size)

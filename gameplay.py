import csv

from interier import Floor, Wall, allsprites
from level_platform import platformgroup
import pygame.sprite
from players import playersgroup

from players import Player, SecondPlayer


class GamePlayScene():
    def __init__(self, parent, filename, screen):
        self.parent = parent
        self.screen = screen
        self.filename = "levels/" + filename
        for el in allsprites:
            el.kill()
        for el in platformgroup:
            el.kill()
        for el in playersgroup:
            el.kill()
        self.load_level()
        running = True
        FPS = 60
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill("green")
            print(allsprites)
            allsprites.draw(self.screen)
            playersgroup.draw(self.screen)
            self.first_player.update()
            playersgroup.update()
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()

    def load_level(self):
        print(playersgroup, platformgroup)
        with open(self.filename, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.board = list(reader)
        self.generate_level()

    def generate_level(self):
        x, y = 0, 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == '.':
                    pass
                elif self.board[x][y] == '#':
                    pass
                elif self.board[x][y] == '@':
                    pass
        self.rows = x
        self.cols = y
        infoObject = pygame.display.Info()
        self.cell_size = min(infoObject.current_h, infoObject.current_w) // max(x, y)
        x, y = 0, 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == '.':
                    Floor(y * self.cell_size+300, x * self.cell_size+100)
                elif self.board[x][y] == '#':
                    pass
                    Wall(y * self.cell_size+300, x * self.cell_size+100)
                elif self.board[x][y] == '@':
                    pass
                # Декодировка символов в классы

        if self.parent.kol == 2:
            x, y = 0, 0  # вопрос
            allsprites = pygame.sprite.Group()
            self.first_player = Player(x, y, allsprites)
            self.second_player = SecondPlayer(x, y, allsprites)
        elif self.parent.kol == 1:
            x, y = 100, 100  # вопрос
            allsprites = pygame.sprite.Group()
            self.first_player = Player(x, y, allsprites)

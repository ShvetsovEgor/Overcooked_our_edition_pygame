import pygame
from load_image import load_image
from platform import Platform


class LevelChoose:
    def __init__(self, kl):
        self.kl = kl
        self.choose_the_level()

    def choose_the_level(self):
        print(232)
        if self.kl == 1 or self.kl == 2:
            infoObject = pygame.display.Info()
            size = width, height = (infoObject.current_w, infoObject.current_h)
            screen = pygame.display.set_mode(size)
            fon = pygame.transform.scale(load_image('fon1.png'), (width, height))
            screen.blit(fon, (0, 0))
            if self.kl == 1:
                f = open('levels1.txt', encoding='utf-8')
            else:
                f = open('levels2.txt', encoding='utf-8')
            lines = f.readlines()
            print(lines)
            kl = lines.count('-----\n') + lines.count('-\n')
            print(kl)
            s = 1
            # пока храним уровни в тхт файле, разделяем их '-----\n' и '-\n'
            # если '-----\n' - уровень не пройден, иначе - пройден.
            # s - количество строк, которые занимает один уровень. Все уровни занимают одинаковое количество строк.
            w = (infoObject.current_w - 100 * (kl + 1)) // kl
            print(infoObject.current_w, w)
            w1 = 15
            for i in range(0, kl, s):
                if lines[i] == '-----\n':
                    Platform(screen, w1, 10, str(i + 1), "red")
                    # pygame.draw.rect(screen, (0, 255, 0),
                    #                  (w1, 300, 100, 100))

                elif lines[i] == '-\n':
                    Platform(screen, w1, 10, str(i + 1), "green")
                    print(w, w1)
                    # pygame.draw.rect(screen, (255, 0, 0),
                    #                  (w1, 300, 100, 100))

                w1 += 100 + w

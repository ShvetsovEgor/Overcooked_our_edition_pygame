import pygame

from food import Plate, Food

pygame.init()
infoObject = pygame.display.Info()
FULLSCREEN = True
if FULLSCREEN:
    size = width, height = (infoObject.current_w, infoObject.current_h)
else:
    size = width, height = (infoObject.current_w - 50, infoObject.current_h - 50)
screen = pygame.display.set_mode(size)

allsprites = pygame.sprite.Group()
platesgroup = pygame.sprite.Group()
foodgroup = pygame.sprite.Group()
put_able = pygame.sprite.Group()
parent = None

# Pizza = Plate(parent, allsprites, platesgroup)
# Pizza += [Food("Тесто", Pizza, allsprites, foodgroup), Food("Томат", Pizza, allsprites, foodgroup, sliced=True),
#           Food('Сыр', Pizza, allsprites, foodgroup, sliced=True)]

Salad = Plate(parent, allsprites, platesgroup, put_able)
Salad += [Food("Томат", Salad, allsprites, foodgroup, sliced=True),
          Food("Огурец", Salad, allsprites, foodgroup, sliced=True)]

# Soup = Plate(parent, allsprites, platesgroup)
# Soup += [Food('Бульон', Soup, allsprites, foodgroup),
#          Food('Мясо', Soup, allsprites, foodgroup, sliced=True, boiled=True),
#          Food('Грибы', Soup, foodgroup, allsprites, sliced=True)]
Steak = Plate(parent, allsprites, platesgroup, put_able)
Steak += [Food('Мясо', Steak, allsprites, foodgroup, sliced=False, fried=True)]
# Burger = Plate(parent, allsprites, platesgroup)
# Burger += [Food('Хлеб', Burger, allsprites, foodgroup),
#            Food('Мясо', Burger, allsprites, foodgroup, sliced=True, fried=True),
#            Food('Сыр', Burger, allsprites, foodgroup, sliced=True),
#            Food('Томат', Burger, allsprites, foodgroup, sliced=True),
#            Food('Салат', Burger, allsprites, foodgroup)]
#
Fish_and_Chips = Plate(parent, allsprites, platesgroup, put_able)
Fish_and_Chips += [Food('Рыба', Fish_and_Chips, allsprites, foodgroup, fried=True, sliced=True),
                   Food('Картофель', Fish_and_Chips, allsprites, foodgroup, sliced=True, fried=True)]
#
# Meat_Burrito = Plate(parent, allsprites, platesgroup)
# Meat_Burrito += [Food('Мясо', Meat_Burrito, allsprites, foodgroup, sliced=True, boiled=True),
#                  Food('Хлеб', Meat_Burrito, allsprites, foodgroup)]
#
# Chicken_Burrito = Plate(parent, allsprites, platesgroup)
# Chicken_Burrito += [Food('Курица', Meat_Burrito, allsprites, foodgroup, sliced=True, boiled=True),
#                     Food('Хлеб', Meat_Burrito, allsprites, foodgroup)]
#
# Stew = Plate(parent, allsprites, platesgroup)
# Stew += [Food('Мясо', Stew, allsprites, foodgroup, fried=True),
#          Food('Картофель', Stew, allsprites, foodgroup, sliced=True, fried=True),
#          Food('Лук', Stew, allsprites, foodgroup, sliced=True, fried=True)]
#
# Smoothie = Plate(parent, allsprites, platesgroup)
# Smoothie += [Food('Банан', Smoothie, allsprites, foodgroup, shaked=True),
#              Food('Арбуз', Smoothie, allsprites, foodgroup, shaked=True),
#              Food('Ананас', Smoothie, allsprites, foodgroup, shaked=True),
#              Food('Клубника', Smoothie, allsprites, foodgroup, shaked=True)]
#
# Sushi = Plate(parent, allsprites, platesgroup)
# Sushi += [Food('Рис', Sushi, allsprites, foodgroup, boiled=True),
#           Food('Рыба', Sushi, allsprites, foodgroup, boiled=True, sliced=True),
#           Food('Нори', Sushi, allsprites, foodgroup),
#           Food('Огурец', Sushi, allsprites, foodgroup, sliced=True)]
#
# Cake = Plate(parent, allsprites, platesgroup)
# Cake += [Food('Мед', Cake, allsprites, foodgroup), Food('Мука', Cake, allsprites, foodgroup),
#          Food('Яйцо', Cake, allsprites, foodgroup), Food('Шоколад', Cake, allsprites, foodgroup, sliced=True)]
#
# Pasta = Plate(parent, allsprites, platesgroup)
# Pasta += [Food('Спагетти', Pasta, allsprites, foodgroup, boiled=True),
#           Food('Рыба', Pasta, allsprites, foodgroup, sliced=True, boiled=True),
#           Food('Креветка', Pasta, allsprites, foodgroup, boiled=True),
#           Food('Томат', Pasta, allsprites, foodgroup, sliced=True)]

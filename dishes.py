from food import Plate, Food
import pygame

allsprites = pygame.sprite.Group()

Pizza = Plate(allsprites)
Pizza += [Food("Тесто", Pizza, allsprites), Food("Томат", Pizza, allsprites, sliced=True),
          Food('Сыр', Pizza, allsprites, sliced=True)]

Salad = Plate(allsprites)
Salad += [Food("Томат", Salad, allsprites, sliced=True), Food("Огурец", Salad, allsprites, sliced=True)]

Soup = Plate(allsprites)
Soup += [Food('Бульон', Soup, allsprites), Food('Мясо', Soup, allsprites, sliced=True, boiled=True),
         Food('Грибы', Soup, allsprites, sliced=True)]

Burger = Plate(allsprites)
Burger += [Food('Хлеб', Burger, allsprites), Food('Мясо', Burger, allsprites, sliced=True, fried=True),
           Food('Сыр', Burger, allsprites, sliced=True), Food('Томат', Burger, allsprites, sliced=True),
           Food('Салат', Burger, allsprites)]

Fish_and_Chips = Plate(allsprites)
Fish_and_Chips += [Food('Рыба', Fish_and_Chips, allsprites, fried=True, sliced=True),
                   Food('Картофель', Fish_and_Chips, allsprites, sliced=True, fried=True)]

Meat_Burrito = Plate(allsprites)
Meat_Burrito += [Food('Мясо', Meat_Burrito, allsprites, sliced=True, boiled=True),
                 Food('Хлеб', Meat_Burrito, allsprites)]

Chicken_Burrito = Plate(allsprites)
Chicken_Burrito += [Food('Курица', Meat_Burrito, allsprites, sliced=True, boiled=True),
                    Food('Хлеб', Meat_Burrito, allsprites)]

Stew = Plate(allsprites)
Stew += [Food('Мясо', Stew, allsprites, fried=True), Food('Картофель', Stew, allsprites, sliced=True, fried=True),
         Food('Лук', Stew, allsprites, sliced=True, fried=True)]

Smoothie = Plate(allsprites)
Smoothie += [Food('Банан', Smoothie, allsprites, shaked=True), Food('Арбуз', Smoothie, allsprites, shaked=True),
             Food('Ананас', Smoothie, allsprites, shaked=True),
             Food('Клубника', Smoothie, allsprites, shaked=True)]

Sushi = Plate(allsprites)
Sushi += [Food('Рис', Sushi, allsprites, boiled=True), Food('Рыба', Sushi, allsprites, boiled=True, sliced=True),
          Food('Нори', Sushi, allsprites),
          Food('Огурец', Sushi, allsprites, sliced=True)]

Cake = Plate(allsprites)
Cake += [Food('Мед', Cake, allsprites), Food('Мука', Cake, allsprites),
         Food('Яйцо', Cake, allsprites), Food('Шоколад', Cake, allsprites, sliced=True)]

Pasta = Plate(allsprites)
Pasta += [Food('Спагетти', Pasta, allsprites, boiled=True), Food('Рыба', Pasta, allsprites, sliced=True, boiled=True),
          Food('Креветка', Pasta, allsprites, boiled=True), Food('Томат', Pasta, allsprites, sliced=True)]

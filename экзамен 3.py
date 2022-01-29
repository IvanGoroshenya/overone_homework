import math
from abc import ABC , abstractmethod


# exam_3_1
# Напишите функцию, которая
# будет принимать номер
# кредитной карты и показывать
# только последние 4 цифры.
# Остальные цифры должны
# заменяться звездочками


# def cart(number):
#
#     return '*' * len(number[:-4]) + number[-4:]
# print(cart('123456789'))


# exam_3_2
# Напишите функцию, которая
# проверяет: является ли слово
# палиндромом

# def palindrom(word):
#     a = word[::-1]
#     if a == word:
#         print('the word is a palindrome')
#     else:
#         print('the word is not a palindrome')
#
#
# print(palindrom('море'))


# exam_3_3
# Напишите классы Круг,Прямоугольник, Квадрат.
# Каждый класс должен содержать метод нахождения площади фигуры.
# Используйте
# :- Наследование - Абстрактный класс
# и методы
# - Округлите площадь круга до 2х чисел после запятой - Число π возьмите из модуля math


class Figure(ABC):
    @abstractmethod
    def area (self):
        pass


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print('Площадь круга равна')
        return round(math.pi * self.radius * self.radius,2 )


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print('Площадь квадрата равна')
        return round(self.side ** 2,2)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print('Площадь прямоугольника равна ')
        return round(self.width * self.length,2)

list_degrees  = [Circle(4.7845),Square(3.78652),Rectangle(2.853,3.86468)]
for i in list_degrees:
    print(i.area())











# Hometask_14_1
# Создать класс Dog.
# Класс имеет четыре
# атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все
# методы
# объекта и вывести на экран все его
# атрибуты.

# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self. weight = weight
#         self.name = name
#         self.age = age
# def jump(self):
#     return f'{self.name} jump'
#
# def run(self):
#     return f'{self.name} run'
#
# def bark(self):
#     return f'{self.name} bark'
#
# def obekt(Dog):
#     return (Dog.__dict__)
# if __name__ == '__main__':
#     Dog = Dog(50, 25, 'Laki', 2)
#
#
#
# print(obekt(Dog))
# print(jump(Dog))
# print(run(Dog))
# print(bark(Dog))


# Hometask_14_2
# Добавить в класс Dog метод change_name.
# Метод
# принимает на вход новое имя и меняет
# атрибут имени у
# объекта. Создать один объект класса.
# Вывести имя.
# Вызвать метод change_name. Вывести имя.

# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self. weight = weight
#         self.name = name
#         self.age = age
#
#
# def change_name (name):
#     Dog.name = 'Tom'
#     return Dog.name
#
# if __name__ == '__main__':
#     Dog = Dog(50, 25, 'Laki', 2)
#
#
# print(change_name(Dog))


# 14.7
# Создайте многоэтажный дом.
# Атрибуты:
# - количество квартир
# Методы:
# - нанять вахтершу

# class House:
#     def __init__(self, floor):
#         self.floor = floor
#
#     def hire(self):
#         print(f'вахтерша нанята')
#
# class House1:
#     def __init__(self, floor, windows, doors):
#         super().__init__(floor)
#         self.windows = windows
#         self.doors = doors
#
#     def build(self):
#         print(f'build')
#
#
# if __name__ == '__main__':
#     House = House(10)
#     print(House.floor)
#     print(House.hire())

# 14.8
# Создайте класс для салона красоты, чтобы можно было
# создавать дома с салоном красоты.
# Методы: - Маникюр - Стрижка
# Методы прописывать не надо,
# просто поставьте заглушку


# class Beauty_salon:
#     def __init__(self,manicure,haircut):
#         self.manicure = manicure
#         self.haircut = haircut
#
#     def manicure(self):
#         pass
#     def haircut(self):
#         pass
#
# class House_with_beauty_salon(Beauty_salon):
#     pass




# 14.9
# Добавьте в салон красоты метод salon_opening_hours, который
# сообщает салон открыт или закрыт.
# Создайте дом с салоном красоты.
# Атрибуты: Час открытия салона
# Час закрытия салона
# Посмотрите работает ли салон в
# 13 часов, а в 23?

# class Beauty_salon:
#
#
#     def __init__(self):
#
#         self.close_time = 18
#         self.opening_time = 9
#
#     def salon_opening_hours(self,time):
#         if self.close_time > time > self.opening_time:
#             print('салон открыт')
#         else:
#             print('салон закрыт')
#
#     def salon_opening_hours1(self,time1):
#         if self.close_time > time1 > self.opening_time:
#             print('салон открыт')
#         else:
#             print('салон закрыт')
#
#
# salon = Beauty_salon()
# salon.salon_opening_hours(12)
# salon.salon_opening_hours1(23)
# print()


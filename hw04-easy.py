# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


num = [random.randint(-100, 100) for _ in range(10)]
num_sqrt = [el**2 for el in num]
print('Исходный список: ', num, '\nНовый список: ', num_sqrt)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_1 = ['яблоко', 'банан', 'виноград', 'клубника', 'манго', 'апельсин']
fruit_2 = ['манго', 'мандарин', 'банан', 'ежевика']
fruit_res = [x for x in fruit_1 if x in fruit_2]
print('Первый список фруктов: ', fruit_1, '\nВторой список фруктов: ', fruit_2, '\nНовый список: ', fruit_res)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

num_3 = [random.randint(-100, 100) for _ in range(30)]
num_res = [x for x in num if x % 3 == 0 and x > 0 and x % 4 != 0]
print('Список чисел: ', num_3, '\nСписок со всеми условиями: ', num_res)

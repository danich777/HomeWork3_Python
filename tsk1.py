# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd

size = int(input('Введите размер списка: '))
my_list = []

for i in range (size):
    my_list.append(rnd(0,10))

print(my_list)
summ = 0
for i in range (1, size, 2):
    summ += my_list[i]
print(summ)
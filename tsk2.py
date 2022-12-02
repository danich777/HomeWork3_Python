# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint as rnd

size = int(input('Введите размер списка: '))
my_list = []

for i in range(size):
    my_list.append(rnd(0,10))
print(my_list)

res_list =[]

for i in range(int(size/2)):
    res_list.append(my_list[i] * my_list[-i-1])

print(res_list)
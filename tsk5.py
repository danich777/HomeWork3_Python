# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib1 = fib2 = 1
my_list = [fib1, fib2]
n = int(input('Введите число: '))

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    my_list.append(fib2)

fib1 = fib2 = 1
for i in range (-n-1, 0):
    fib1, fib2 = fib2, fib1 - fib2
    my_list.insert(0,fib2)

print(my_list)
# coding: utf-8

# Ввод двух чисел с консоли
num1, num2 = map(int, input().split())

# Проверка и вывод наименьшего числа
if num1 < num2:
    print(num1)
else:
    print(num2)

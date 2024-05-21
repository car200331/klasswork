#coding: utf-8

# Ввод числа
number = int(input("Введите четырехзначное число: "))

# Проверка, является ли число четырехзначным и делится ли на 7 или 17
if 1000 <= number <= 9999 and (number % 7 == 0 or number % 17 == 0):
    print("YES")
else:
    print("NO")
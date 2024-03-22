#coding: utf-8
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if a < b:
    print("Меньшее число:", a)
elif b < a:
    print("Меньшее число:", b)
else:
    print("Числа равны")
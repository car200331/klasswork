#coding: utf-8
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))
if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) and (a % 2 != 0 or b % 2 != 0 or c % 2 != 0):
    print("yes")
else:
    print("no")
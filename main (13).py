#coding: utf-8
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
expected_sum = float(input("Введите предполагаемую сумму: "))
actual_sum = num1 + num2
if actual_sum == expected_sum:
    print("Верно! Результат сложения {} и {} равен {}".format(num1, num2, expected_sum))
else:
    print("Неверно! Правильный результат сложения {} и {} равен {}".format(num1, num2, actual_sum))
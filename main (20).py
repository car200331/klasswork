#coding: utf-8
number = input("Введите четырехзначное число: ")

if len(number) != 4 or not number.isdigit():
    print("Некорректный ввод.")
else:
    first_digit = int(number[0])
    second_digit = int(number[1])
    third_digit = int(number[2])
    fourth_digit = int(number[3])

    if first_digit + fourth_digit == second_digit - third_digit:
        print("ДА")
    else:
        print("НЕТ")

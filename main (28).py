#coding: utf-8

# Константа для перевода дюймов в сантиметры
inch_to_cm = 2.54

# Вывод заголовка таблицы
print("Дюймы  Сантиметры")

# Цикл для значений от 10 до 22 дюймов
for inches in range(10, 23):
    centimeters = inches * inch_to_cm
    print(f"{inches:5}  {centimeters:10.2f}")
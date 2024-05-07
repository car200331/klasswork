#coding: utf-8
calories = float(input("Введите количество калорий в продукте: "))
sugar = float(input("Введите количество сахара в продукте: "))
max_calories_per_meal = 500
max_sugar_per_meal = 25
if calories <= max_calories_per_meal and sugar <= max_sugar_per_meal:
    print("Можно есть! Этот продукт подходит для здорового питания.")
else:
    print("Не стоит есть этот продукт. Превышены допустимые значения калорий или сахара.")
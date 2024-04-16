 #coding: utf-8
color1 = input().strip().lower()
color2 = input().strip().lower()

if color1 == "красный" and color2 == "синий" or color1 == "синий" and color2 == "красный":
    print("фиолетовый")
elif color1 == "красный" and color2 == "жёлтый" or color1 == "жёлтый" and color2 == "красный":
    print("оранжевый")
elif color1 == "синий" and color2 == "жёлтый" or color1 == "жёлтый" and color2 == "синий":
    print("зелёный")
elif color1 == color2:
    print(color1)
else:
    print("ошибка цвета")
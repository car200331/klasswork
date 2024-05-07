# coding: utf-8
distance_to_destination = float(input("Введите расстояние до места назначения (в км): "))
current_time_of_day = int(input("Введите текущее время суток (часы): "))
walking_threshold = 2  # в км
biking_threshold = 5   # в км
public_transport_threshold = 10  # в км
if distance_to_destination <= walking_threshold:
    print("Вы можете дойти до места назначения пешком.")
elif distance_to_destination <= biking_threshold:
    if 7 <= current_time_of_day <= 19:  # день
        print("Лучше взять велосипед.")
    else:
        print("Велосипед может быть хорошим вариантом, если есть хорошая освещенность на пути.")
elif distance_to_destination <= public_transport_threshold:
    if 7 <= current_time_of_day <= 19:  # день
        print("Можно воспользоваться общественным транспортом.")
    else:
        print("Общественный транспорт может быть более надежным и безопасным вечером.")
else:
    print("Рекомендуется использовать автомобиль или другие средства дальней связи.")
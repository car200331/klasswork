#coding: utf-8
genre = input("Введите жанр книги: ")
rating = float(input("Введите рейтинг книги: "))

if genre == "фантастика" and rating > 4:
    print("Стоит прочитать!")
elif genre == "роман" and rating > 3:
    print("Можете попробовать прочитать.")
elif genre == "детектив" and rating > 4:
    print("Это должно быть интересно.")
elif genre == "исторический" and rating > 4:
    print("Это обязательно к прочтению.")
else:
    print("Возможно, стоит поискать что-то другое.")
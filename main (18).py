 #coding: utf-8
 # Ввод возраста пользователя
user_age = int(input("Введите возраст пользователя: "))

# Определение возрастной группы
if user_age <= 13:
    age_group = "детство"
elif 14 <= user_age <= 24:
    age_group = "молодость"
elif 25 <= user_age <= 59:
    age_group = "зрелость"
else:
    age_group = "старость"

# Вывод результата
print("Возрастная группа:", age_group)
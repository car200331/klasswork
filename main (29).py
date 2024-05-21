#coding: utf-8
exchange_rate = float(input("Введите текущий курс доллара к рублю: "))
print("Доллары  Рубли")
for dollars in range(1, 21):
    rubles = dollars * exchange_rate
    print(f"{dollars:7}  {rubles:10.2f}")
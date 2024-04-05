#coding: utf-8
password = input().strip()
confirm_password = input().strip()

if password == confirm_password:
    print("пароль принят")
else:
    print("пароль не принят")
# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Введите номер дня недели: "))

if 1<=day<6:
    print("Workday")
elif day==6 or day==7:
    print("Weekend")
else:
    print("It's not a day of the week!")
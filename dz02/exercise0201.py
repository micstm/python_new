# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

num = float(input("Введите число: "))
rez = 0

num_int = int(num // 1)
acc = len(str(num)) - 1 - len(str(num_int))
num_float = float(f"{num % 1:.{acc}f}")
num_float_int = num_float * 10 ** acc

while num_int > 0:
    rez = rez + (num_int % 10)
    num_int = int(num_int // 10)

while num_float_int > 0:
    rez += num_float_int % 10
    num_float_int = int(num_float_int // 10)

print(rez)

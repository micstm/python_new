# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011


def dec_bin(num_dec):
    num_bin = 0
    count = 1
    while num_dec > 0:
        num_bin += (num_dec % 2) * count
        count *= 10
        num_dec //= 2
    print(num_bin)


dec_bin(int(input('Input number: ')))


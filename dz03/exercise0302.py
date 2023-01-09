# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample


def calculate(amount):
    new_list = sample(range(1, amount + 1), k=amount)
    print(new_list)
    rez_list = []
    for i in range(amount // 2):
        rez_list.append(new_list[i] * new_list[-(i+1)])
    if (amount % 2) != 0:
        rez_list.append(new_list[amount // 2])
    print(rez_list)


calculate(int(input('Enter amount - ')))


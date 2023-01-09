# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
# out
# [4, 2, 4, 9]
# 8


from random import sample


amount = (int(input('Enter amount - ')))

new_list = sample(range(1, amount + 1), k=amount)
print(new_list)
s = 0
for i in range(0, amount, 2):
    s += new_list[i]
print(s)


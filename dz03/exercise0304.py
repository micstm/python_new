# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
#
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36


from random import uniform


def fill_float(num):
    new_list = []
    for i in range(num):
        new_list.append(round(uniform(1, 10),2))
    print(new_list)
    n_min = 1
    n_max = 0
    for i in range(num):
        temp = round((new_list[i] - new_list[i] // 1), 2)
        if n_min > temp:
            n_min = temp
        if n_max < temp:
            n_max = temp
    n_diff = round((n_max - n_min), 2)
    print('Min: ', n_min,', Max: ', n_max,', Difference: ,', n_diff)


fill_float(int(input('Input number: ')))


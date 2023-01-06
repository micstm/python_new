# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071


num = int(input('Введите число: '))

spisok = []
summ = 0

for n in range(1, num+1):
    i = float(f"{(1 + 1/n) ** n:.3f}")
    summ += i
    spisok.append(i)
print(spisok)
print(summ)

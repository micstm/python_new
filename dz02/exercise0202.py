# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]


num = int(input("Введите число: "))

spisok = []

for i in range(1, num+1):
    k = 1
    for j in range(1, i+1):
        k = k * j
    spisok.append(k)
print(spisok)
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), н
# е превосходящие числа N.

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
i += 1
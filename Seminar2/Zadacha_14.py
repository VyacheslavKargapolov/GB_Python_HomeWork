"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N."""

N = int(input("Введите число N: "))
i = 0

print("Все целые степени двойки, не превосходящие числа", N)
while 2**i <= N:
    print ("2 ^",i, "=", 2**i)
    i +=1
    
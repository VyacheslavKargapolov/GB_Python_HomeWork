"""Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его."""
list_1 = [10, 12, 37, 44, 45]
k = 24
L = len(list_1)
i = 1
S = abs(list_1[0] - k)
while i < L:
    if abs(list_1[i] - k) < S:
        S = abs(list_1[i] - k)
        rez = list_1[i]
    i +=1
print(rez)
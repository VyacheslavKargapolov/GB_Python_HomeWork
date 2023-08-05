"""Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 1, 2, 5
Вывод: 1, 3, 5, 7, 9 """


def arifmetic_progress(el1, count, raznost):
  res = []
  for count in range(1, count+1):
    el = int(el1 + (count-1)*raznost)
    res.append(el)
  return(res)

a1 = int(input("Введите первый элемент последовательности: "))
n = int(input("Введите количество элементов последовательности: "))
d = int(input("Введите разность элементов арифметической последовательности: "))

s =  arifmetic_progress(a1, n, d)
print()
print("Последовательность арифметической прогрессии:")
print(*s)
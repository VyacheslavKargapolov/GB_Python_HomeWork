""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть """

import random
print("Введите количество монет на столе:")
n = int(input())
a = random.randint(0, n)
b = n - a
print()
print(f"монет вверх решкой ", a)
print(f"монет вверх гербом ", b)
print()
print("для того, чтобы все монеты лежали одной стороной вверх, ")
if a > b:
    print(f"необходимо перевернуть ", b, "монет")
else:
    print(f"необходимо перевернуть ", a, "монет")
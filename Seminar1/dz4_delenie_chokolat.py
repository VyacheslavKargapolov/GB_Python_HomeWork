'''Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.'''

a = 4
b = 3
c = 12

if (c%a == 0 or c%b == 0) and c <= a*b and c > 0:
    print('yes')
else:
    print("no")

'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
 Выведите минимальное количество монет, которые нужно перевернуть
'''

n = int(input('Введите количество монеток которые лежат на столе: '))
heads = 0
tails = 0
for i in range(n):
    x = int(input('Введите орел или решка. Орел = 1, Решка = 0: '))
    if x == 0:
        heads += 1
    elif x == 1:
        tails += 1
    else:
        print('Повторите ввод')
if tails > heads:
    print(heads)
elif heads >= tails:
    print(tails)


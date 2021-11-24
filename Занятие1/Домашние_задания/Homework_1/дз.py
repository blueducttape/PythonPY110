"""Задачи по map"""
"""Задание 1.
Напишите программу Python, которая преобразует
 все символы в верхний и нижний регистры и
удаляет повторяющиеся буквы из заданной 
последовательности. Используйте функцию map ()."""


_lst = {'U', 'f', 'a', 'b', 'i', 'o', 'E'}
print(tuple(map(lambda x: (x.upper(), x.lower()), set(_lst))))


"""Задание 2.
Напишите программу Python
для разделения заданного словаря списков на список словарей с помощью функции map()."""
d = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
*a, = map(lambda x: dict(zip(d.keys(), x)),  zip(*d.values()))
print(a)

"""Задание 3.
Напишите скрипт для преобразования заданного списка кортежей в список строк с помощью функции map()."""
listoftuples = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(list(map(" ".join, listoftuples )))


"""Задачи по лямбдам"""

'''  Задание 1.Реализуйте функцию mod_checker(x, mod=0), которая
будет возвращать лямбда функцию от одного аргумента y, которая будет
 возвращать True, если остаток от деления y на x равен mod, и False иначе'''


def mod_checker(x, mod=0):
    return lambda y: y % x == mod


if __name__ == '__main__':
    mod_3 = mod_checker(3)
    print(mod_3(3))
    print(mod_3(4))

    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4))

'''Задание 2.
Напишите скрипт для сортировки списка кортежей по второму элементу с помощью Lambda.'''
tuple_list = [("HTML", 15, 'M01'), ("JavaScript", 10, 'M03'), ("Bootstrap", 5, 'M02')]
sorted_list = sorted(tuple_list, key=lambda x: x[1])
print(sorted_list)


text = ["php", "w3r", "Python", "abcd", "  Java "," aaa "]
result = list(filter(lambda x: (x == " ".join(reversed(x))), text))
print  (" Список палиндромов:", result)

'''Задание 3.
Напишите скрипт для извлечения года, месяца, даты и времени
 с помощью Lambda. В реализации используйте модуль datetime.'''

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))



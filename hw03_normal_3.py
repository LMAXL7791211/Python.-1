# hw 3 normal Лукьянов Максим
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#print(list(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])))



def myownfilter(func, sequence):
    res = []
    for el in sequence:
        if func(el):
            res.append(el)
    return res

print (myownfilter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14]))
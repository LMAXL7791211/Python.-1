# hw 3 normal Лукьянов Максим
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m): #невнимательно прочитал условие, сделал функцию, печатающую ряд
    for i in range(1,m+1):
        fibrow.append(fibrow[i]+fibrow[i+1])
        if i>=n:
            print(fibrow[i], end=' ')

def fibonacci2(n, m): # переписал, return не делал, без него список "вернулся"
    for i in range(1,m+1):
        fibrow.append(fibrow[i]+fibrow[i+1])
        if i>=n:
            fibrow_ab.append(fibrow[i])

#pass

fibrow = [0,1,1] #добавил ноль в нулевой индекс, чтобы номер индекса и номер ряда совпадал.
fibrow_ab = []

try:
    a = int(input("Введите число - номер начального элемента списка"))
    b = int(input("Введите число - номер конечного элемента списка"))
    if a >= b or a < 1:
        print("Неверные числа")
        exit(1)

    #fibonacci(a,b)
    fibonacci2(a,b)

    #print(fibrow)
    print("Ряд Фибоначчи начиная с ", a, "-го номера и до номера ", b)
    print(fibrow_ab)
except ValueError:
    print("Ошибка в формате данных")
    exit(1)
# name = "admin"  # можно задавать переменную без каких либо дополнительных слов вроде let
# #  Переменная может начинаться с _ или буквы. Цифра в конце. Спец символы не допускаются.
# print("Hello", name)  # ctr+alt+l - форматирование
# age = 20.2
# print(age)
# print(type(name))  # Type-тип данных. Print(type(name)) ctrl+d - дубликат.
# print(type(age))
# a = 4
# b = 5
# print(a, id(a))  # ID - уникальный адрес элемента
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# a = 5
# b = 3
# print(a)
# print(b)
# a = b = c = 5  # Выполняется справа налево. Одно и то же значение нескольким переменным
# print(a, b, c)
# a, b, c = 7, "Hello", 9.2  # Присваиваемое переменным разных значений
# print(a, b, c)
# import random

# PI = 3.14
# print(PI)
# PI = 2  # Нарушение соглашения между программистами
# print(PI)

# a = 5
# b = "7"
# print(a + int(b))  # int()-преобразование к формату числа
# print(str(a) + b)  # str()-преобразование к формату строки
#
# a = 1
# b = 2
# print("a:", a)  # запятая позволяет записывать добавляя пробел
# print("b:", b)
# a, b = b, a
# # с = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1
#
# print("строка \n"
#       "символов")  # кавычки будут отрабатывать одинаково
# print('строка символов строка символов строка символов строка символов строка символов строка символов строка '
#       'символов строка символов строка символов')
# print("\"program\" \rC:\\folder\\file.txt")  # Экранирование кавычек и спец символы через \. \r - затирает
# # все, что было до него
#
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"  # конкатенация
# print(s3)
# print(s3 * 3)  # копирование столько раз на сколько умножили
#
# # Арифметические операторы
#
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 + 2)
# print(6 / 2)
# print(5 / 2)
# print(5 // 2)  # целочисленное деление
# print(6 // 2)
# print(6 ** 2)
# print(5 % 2)
#
# a, b, c = 5, 7, 3
# sum1 = a + b + c
# print("Сумма:", sum1)
# print("Произведение:", a * b * c)
# print("Средне арифметическое:", sum1 / 3)
#
# numbers = 6 + 4 * 5 ** 2 + 7  # приоритет операторов
# print(numbers)
#
# numbers = (6 + 4) * (5 ** 2 + 7)  # приоритет операторов
# print(numbers)
#
# num = 10
# num += 5  # num = num + 5
# print(num)
#
# num -= 3  # num = num + 3
# print(num)
#
# num *= 4  # num = num * 4
# print(num)

# Дано четырехзначное число. Необходимо вывести его в обратной последовательности

# num = 4321
# a = num % 10  # 1
# print(a)
# num = num // 10  # 432
# # print("num: ", num)
# b = num % 10  # 2
# print(b)
# num = num // 10  # 43
# # print("num: ", num)
# c = num % 10  # 3
# print(c)
# num = num // 10  # 4
# d = num % 10  # 4
# print(d)
# num = a * 1000 + b * 100 + c * 10 + d
# print("num:", num)

# num = 4321
# res = num % 10 * 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# print(int(3.8))  # Перевод в другой тип данных. Округления не происходит
# print(round(3.8))  # 4 Округление согласно законам математики. Тип int
# print(round(3.8565634, 2))  # 3.85 кругление согласно законам математики до указанного знака после запятой. Тип float


# a = '5.2'
# b = 10
# c = int(a) + b
# print(c)


# name = "Виктор"
# age = 28
# print("Меня зовут", name, ".Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ".Мне", age, "лет.", sep="___", end="\n\n")  # sep="" меняет запятые разделители на
# # символ
# print("Hello")


# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power

# print("Число", num, "в степени", power, "равно:", res)

# Запросите у пользователя 4 числа. СЛожить. Разделить 1ую сумму на 2ую. 2 цифры после запятой

# a = int(input("Введите 1ое число: "))
# b = int(input("Введите 2ое число: "))
# c = int(input("Введите 3е число: "))
# d = int(input("Введите 4ое число: "))
# res = round(((a + b)/(c + d)), 2)
# print(res)


# b1 = True  # при арифметике преобразовывается к 1
# b2 = False  # при арифметике преобразовывается к 0
# print(b1 + 5)  # 1+5
# print(b2 + 5)  # 0+5
# print(type(b1))
#
# print(bool("python"))
# print(bool(""))  # пустые кавычки дадут False
# print(bool(10))
# print(bool(0))  # 0 или 0.0 даст False
# print(bool(False))  # False даст False
# print(bool(None))  # None даст False
#
# test = None
# print(test, type(test))
# test = 5
# print(test, type(test))


# print(7 == 7)
# print(7 == '7')
# print(2 + 5 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" > "ПРИВЕТ")  # Сравнивает через ASCII

# print(2 < 4 < 9)  # True : True => True
# print(2 < 4 > 9)  # True : False => False
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 < 2 or 1 + 3 < 4)
# print(not 9 - 5)  # not инвертирует на противоположное значение
# print(not 9 - 9)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# PEP20
# import this

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")
#

# a = input("Введите 1-сторону: ")
# b = input("Введите 2-сторону: ")
# c = input("Введите 3-сторону: ")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# Вложенные условия

# day = int(input("Введите день недели(цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует!")


# Написать программу, которая предполагает пользователю ввести ворон. А потом вывести кол-во и верный падеж для ворон

# n = int(input("Введите количество ворон на ветке: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin1"
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")


# day = 'суббота'
# time = 11
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье' if 9 <= time <= 12:
#         print("Рабочий выходной день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# Тернарное выражение

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a, b = int(input("Введите 1ое число: ")), int(input("Введите 2ое число: "))
# print("на 0 делить нельзя" if a == 0 or b == 0 else a/b)


# Исключения. Exceptions
# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # кортеж
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# # except (ValueError, ZeroDivisionError):  # кортеж
# #     print("Нельзя вводить строки и нельзя делить на ноль")
# # else:  # когда в блоке try не возникло исключений
# #     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае. Может быть try + finally
#     print("Конец программы")


# n = input("Введите 1ое число: ")
# m = input("Введите 2ое число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# Цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     # i = i +1
#     i += 1


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1


# n = int(input("Указать кол-во символов"))
# print("*" * n)
# print("+-" * int(n / 2))


# n = int(input("Указать кол-во символов"))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1


# n = int(input("Указать кол-во символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Указать кол-во символов: "))
# while n > 0:
#         print("*", end="")
#         n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)


# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue  # пропускает текущую итерацию
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл j =", j)
#         j += 1
#     i += 1


# #  Таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# j = 0
# while j < 5:
#     print(" " * j, "*", sep="")
#     j += 1


# i = 0  # 1
# while i < 5:  # 1 < 5
#     j = 0  # 0
#     while j < i:  # 0 < 1
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# for element in collection:
#     print(element)

# for i in "Hello":  # Находится в строке, коллекция или итерируемый объект
#     print(i)

# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)


# print(range(2, 5, 2))
# range(start, stop, step) start = 0, step = 1

# for i in range(9, 0, -1):
#     print(i, end=" ")
#
# print()
#
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# for i in range(100, 0, -10):
#     print(i, end=" ")


# a = int(input("Введите целое число: "))
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")


# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:
#     print("done")


# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")


# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     # for j in range(w):
#         print("*", end="")
#     print()


# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# print([i * 5 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])


# num = [9, 3, 8, 4, 1, "Hello", 2.3, True]
# print(num)
# # print(type(num))
# # print(num[0])
# # print(num[2])
# # print(num[-2])
# # print(num[7])
# # # print(num[8])
# # num[1] = 100
# # num[2] += 50
# # print(num)
# print(len(num))


# nums = list("Hello")
# nums = list(range(2, 21, 2))
# print(nums)  # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
# print(type(nums))


# nums = list("Hello")
# num = nums * 2
# print(num + [1, 2, 3])


# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])


# генератор списков
# [выражение for переменная in последовательность]
# a = [0 for i in range(5)]
# print(a)
# b = [i ** 2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in "list"]
# print(c)


# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("Введите число: "))
#     print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)


# b = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# print("Среднее арифметическое: ", round(sum(b) / len(b), 1))
# print("Минимальное число: ", min(b))
# print("Максимальное число: ", max(b))


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:  # получаем доступ к введенному элементу
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)


# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):  # i = 0 1 2 3 4 5 6 7 8
#     print(lst[i], end=" ")
# print()
# for i in lst:
#     print(i, end=" ")  # i = 10 20 30 40 50 60 70 80 90


# colors = ['red', 'blue', 'green']
# for i in range(len(colors)):
#     print(colors[i], end=" ")
# print()
# for i in colors:
#     print(i, end=" ")


# n = list(range(21, 41))
# print(n)
# count = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print()
# print("Кол-во четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", s)


# n = [4, 9, 6]
# print(n)
# i = 2
# print(n[i])
# print(n[i - 1])


# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# print(a)
# for i in a:
#     if i > i - n:
#         print(i, end=" ")

# a = [7, 9, 3, 1, 2]
# print(a)
# print(id(a[0]))
# print(id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(a)
# print(id(a[0]))
# print(id(a[1]))


# Срезы - список[start:stop:step] step не обязательный параметр
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# print(s[1:3])
# print(s[::2])
# print(s[::-1])
# print(s[5::-1])
# i = 5
# while i >= 0:
#     print(s[i])
#     i -= 1

# s = [6, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[5:6]
# print(b, id(b))


# s = "Hello World!"
# print(s[6:-1])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1:])
# print(s[-1:])
# print(s[3:4:])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2] = 50  # если мы изменяем 1 конкретный элемент, к которому обращаемся можем использовать 1 число без скобок
# print(s)
# s[2:5] = []
# del s[1]  # функция удаления
# print(s)


# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# s[len(s):] = [12]
# print(s)

# Методы списка
# dir(list)
# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# s.append(12)  # Добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # Добавляет любое количество элементов в конец списка
# print(s)
# s.append("add")
# print(s)
# s.extend("add")
# print(s)
# s.insert(3, "Hello")  # Добавляет элемент(второй параметр) в список в заданный индекс(первый параметр)
# print(s)
# s.insert(20, 90)   # Стараемся не использовать
# print(s)


# a = [int(input("Введите кол-во итераций: ")) for i in range(int(input("Введите число: ")))]
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # 2, 1, 4, 3
#
# # for i in a:  # 5, 9, 2, 1, 4, 3
# #     for j in b:  # 4, 2, 1, 3, 7
# #         if i in c:
# #             continue
# #         if i == j:
# #             c.append(i)
# #             break
# # print(c)
#
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)


# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# b = []
# for i in range(0, len(a)):
#     if (a[i] % 3) == 0:
#         b.extend(a[i])
#         print(b)
#     else:
#         print(a[i], "Не делится на 3 без остатка.")

# a = [int(input("-> ")) for i in range(int(input("n= ")))]
# b = []
# for i in range(0, len(a)):
#     if (a[i] % 3) == 0:
#         b.extend(a[i])
#         print(b)
#     if a[i] % 3 != 0:
#         print(a[i], "Не делится на 3 без остатка.")


# a = int(input("-> "))
# while True:
#     n = list(input("n= "))
#     while len(n) <= a:
#         if n % 3 != 0:
#             print(n, "Не делится на 3 без остатка.")
#         if n % 3 == 0:
#             print(n)


# s = []
# n = int(input("Кол-во итераций: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится без остатка")


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
# # if len(b) > len(a):
# #     for i in range(len(a)):  # 0-3
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):  # range(3, 5)
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(b), len(a)):  # range(3, 5)
# #         c.append(a[i])
# # print(c)
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):  # 0-3
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5)
#     c.append(b[i])
# print(c)


# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# # n = 2
# # if n in a:
# #     # a.remove(n)  # удаляет из списка конкретное значение. Выбрасывает исключение, если элемента не существует
#
# last = a.pop()  # удаляет последний(или по индексу) элемент из списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1)
# print(second)
# print(a)
# a.clear()  # очищает список от элементов
# print(a)


# # s = []
# # n = int(input("Кол-во итераций: "))
# # for i in range(n):
# #     x = int(input("Введите число: "))
# #     s.append(x)
# # y = int(input("Введите индекс: "))
# # s.pop(y)
# # print(s.pop(y))
#
# sp = [int(input("-> ")) for i in range(int(input("Введите количество чисел списка: ")))]
# x = int(input("Введите индекс: "))
# print(sp.pop(x))
# print(sp)


# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)  # возвращает количество заданных значений в списке
# print(num)
# ind = a.index(3, 3, -1)  # возвращает индекс(первый по счету) заданного значения
# print(ind)
# a.reverse()  # разворачивает список в противоположную сторону
# print(a)
# a.sort()  # сортировка списка
# print(a)
# a.sort(reverse=True)  # сортировка списка от большего к меньшему
# print(a)


# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(reverse=True)
# print(s)
# s.sort(reverse=True, key=len)
# print(s)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# n = (sorted(a))  # возвращает новый отсортированный список. Можем положить в переменную
# print("n =", n)
# print(a)

# a = [1, 2, 3]
# b = a.copy()  # .copy дубликат списка со своим уникальным адресом памяти
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))


# Генерация случайных данных

# import random
#
# print(random.random())  # генерирует случайное значение от 0 до 1
# print(random.randint(0, 9))  # генерирует от числа до числа(включая)
# print(random.randrange(2, 9, 2))  # randrange(start, stop, step)
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)


# mas = [random.randint(0, 100) for i in range(10)]
# # mas = ["a", "b", "c"]
# print(mas)
# print(len(mas))  # работает со строками
# print(min(mas))  # работает со строками
# print(max(mas))  # работает со строками
# print(sum(mas))
#
# s = 0
# for i in mas:
#     s += i
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# m = max(mas)
# print("max:", m)
# mas.remove(m)
# mas.insert(0, m)
# print(mas)

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)


# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# minimum = min(array)
# print("Min: ", min(array))
# ind = array.index(minimum)
# print(ind)
# # print(array[ind+1:])
# del array[:ind]
# print(array)


# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
# if not lst:
#     print("Список пустой")


# lst = [5, 6, 8, 9, 7]
# # if len(lst) == 0:
# #     print("Список пустой")
# if not lst:
#     print("Список пустой")
# print(5 not in lst)

# import random
#
# n1 = int(input("Введите размер 1ого списка: "))
# n2 = int(input("Введите размер 2ого списка: "))
# a = [random.randint(0,10) for i in range(n1)]
# b = [random.randint(0,10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Элементы обоих списков:", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Повторяющиеся элементы списка:", c)
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальное и максимально значения из списков", c)


# Вложенные списки-матрицы

# m = [
#     [1, 2, 3, 4, 9, 8],
#     [5, 6, 7, 8, 3],
#     [9, 10, 11, 12]
# ]
# # print(m)
# # print(len(m))
# # print(m[1][2])
# # print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
#
# # matrix = []
# # for y in range(h):
# #     new_row = []
# #     for x in range(w):
# #         new_row.append(0)
# #     matrix.append(new_row)
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# for x, y, in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, y)
#     print(x, "+", y, "=", x + y)

# import random
#
# w, h = 5, 3
# matrix = [[random.randint(1, 100) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()


# import random
# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)


# Modules

# import math
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))
# print(math.floor(3.8))


# import math as m
#
# print(m.ceil(3.2))
# print(m.floor(3.8))


# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.8))


# from math import *
# print(ceil(3.2))
# print(floor(3.8))


# from math import pi
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности", round(2 * pi * radius, 2))


# from math import sqrt
# a = int(input("Введите первый катет: "))
# b = int(input("Введите второй катет: "))
# print(sqrt(a ** 2 + b ** 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "bel")

# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(4645545))
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("Сегодня: %B %d, %y"))
# print(time.strftime("%B %d, %Y", time.localtime(5744664461)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))

# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# print()


# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")

#
# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res ** 2)
# n = 6
# m = 3
# get_sum(n, m)
# get_sum('abc', 'def')


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# m = maximum(9, 16)
# print(m)

# def foo(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# c = foo(int(input()), int(input()))
# print(c)

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
#


# def func(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(func(10, 5))
# print(func(5, 10))
#
# a = 5
# b = 10
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":  # 65 <= 97 <= 90
#             has_upper = True
#         if "a" <= ch <= "z":  # 65 <= 97 <= 90
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param(7)
# a = "#"
# set_param(s=a)


# def digit_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s


# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))
#
# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

# a = "Hello"
# b = "Hello"
# b = b + "_new"
# print(a == b)
# print(a is b)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)


# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

# Картежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = "red", "blue", "green"
# print(a)
# print(type(a))
#
# a = (1, 2, 3, 4, 5)
# print(a)
# print(type(a))
#
# a = (5,)
# print(a)
# print(type(a))


# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])

# figure = input("1 -, 2 -, 3 - :")
# if figure == "1":
#     rectangle()
# elif figure == "2":
#     triangle()
# elif figure == "3":
#     circel()

# s = [i for i in range(5)]
# print(s)
# s=tuple(input("-->") for i in range(5))
# print(s)

# from random import randint
# s = tuple(randint(20, 40) for i in range(5))
# print(s)

# res = tuple(2 ** i for i in range(1, 13))
# print(res)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# # print(t3.count('l'))
# # print(t3.count('a'))
# # # print(t3.index('l', 4))
# # ch = "a"
# # try:
# #     print(t3.index(ch))
# # except ValueError:
# #     print("Такого символа в кортеже не существует")
#
# for i in t3:
#     print(i, end=" ")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def run(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# def foo(a, b):
#     res = a + b
#     c = res.count(0)
#     return res, c
#
#
# tpl1 = run(0, 5)
# tpl2 = run(-5, 0)
# print(tpl1)
# print(tpl2)
# print(foo(tpl1, tpl2))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)


# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = (func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4]))
# print("Сумма:", a)
# print("Кол-во:", b)
#
#
# for i in "red", "blue", "green":
#     print(i)


# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# множество (set)

# s = {'banana', 'apple', 'orange'}
# print(s)
# print(type(s))
# for i in s:
#     print(i)


# a = set("Hello")
# print(type(a))
# print(a)


# s = {i * i for i in range(15)}
# print(s)


# a = set("Hello")
# print(a)
# print('o' in a)
# print('a' in a)
# a.add("a")
# print(a)
# a.remove('e')
# print(a)
#
#
# git init - создание нового репозитория

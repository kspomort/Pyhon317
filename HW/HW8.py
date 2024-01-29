from math import pi


def circle(r):
    return pi * r ** 2


def rectangle(a, b):
    return a * b


def triangle(a, b):
    return 0.5 * a * b


figure = input("Выберите фигуру:"
               "\n 1 - прямоугольник"
               "\n 2 - треугольник"
               "\n 3 - круг"
               "\n : ")

if figure == "1":
    h = float(input("Длина: "))
    w = float(input("Ширина: "))
    print("Площадь прямоугольника: ", round(rectangle(h, w), 2))
elif figure == "2":
    base = float(input("Введите Основание: "))
    h = float(input("Введите Высоту: "))
    print("Площадь треугольника: ", round(triangle(base, h), 2))

elif figure == "3":
    rad = float(input("Радиус: "))
    print("Площадь круга: ", round(circle(rad), 2))
else:
    print("Ошибка! Необходимо ввести цифру от 1 до 3!")
    figure = input("Выберите фигуру:"
                   "\n 1 - прямоугольник"
                   "\n 2 - треугольник"
                   "\n 3 - круг"
                   "\n : ")


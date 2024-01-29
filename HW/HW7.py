from math import pi, sqrt

x = float(input("Выберите фигуру:"
                "\n 1 - треугольник"
                "\n 2 - прямоугольник"
                "\n 3 - круг"
                "\n : "))
if x == float(1):
    a = float(input("Введите 1ую сторону: "))
    b = float(input("Введите 2ую сторону: "))
    c = float(input("Введите 3ю сторону: "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника: ", round(s, 2))
if x == float(2):
    h = float(input("Введите 1ую сторону: "))
    w = float(input("Введите 2ую сторону: "))
    print("Площадь прямоугольника: ", round((h * w), 2))
if x == float(3):
    radius = float(input("Введите радиус: "))
    print("Площадь круга: ", round((pi * radius * radius), 2))

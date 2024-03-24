class Area:
    __ct = 0

    @staticmethod
    def ar_sq(a):
        Area.__count()
        return a ** 2

    @staticmethod
    def ar_geron(a, b, c):
        Area.__count()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

    @staticmethod
    def ar_rect(a, b):
        Area.__count()
        return a * b

    @staticmethod
    def ar_triangle(a, b):
        Area.__count()
        return 1 / 2 * a * b

    @staticmethod
    def __count():
        Area.__ct += 1

    @staticmethod
    def count():
        return Area.__ct


sq = Area
print(f"Площадь треугольника по формуле Герона (3,4,5): {sq.ar_geron(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту (6,7): {sq.ar_triangle(6, 7)}")
print(f"Площадь квадрата (7): {sq.ar_sq(7)}")
print(f"Площадь прямоугольника (2,6): {sq.ar_rect(2, 6)}")
print(f"Количество подсчётов площади: {sq.count()}")
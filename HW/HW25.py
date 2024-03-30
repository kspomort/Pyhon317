class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def mult(self):
        return self.a * self.b

    def sum(self):
        return self.a + self.b


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hyp(self):
        hyp = round((self.a**2 + self.b**2) ** (1/2), 2)
        return hyp

    def sq(self):
        sq = (self.a * self.b) * (1/2)
        return sq

    def print_info(self):
        print(f"Гипотенуза △ABC: {self.hyp()}")
        print(f"Прямоугольный треугольник △ABC: {self.a, self.b, self.hyp()}")
        print(f"Площадь △ABC: {self.sq()}\n")


f = RightTriangle(5, 8)
f.print_info()
print("Сумма:", f.sum())
print("Произведение:", f.mult(), end=" ")

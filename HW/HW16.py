# def decor(fn):
#     def wrap(*args):
#         return print("Среднее Арифметическое чисел:", ", ".join(map(str, args)), "=", fn(*args) / len(args))
#
#     return wrap
#
#
# @decor
# def func(*args):
#     summa = sum(args)
#     print(c, ", ".join(map(str, args)), "=", summa)
#     return summa
#
#
# func(2, 3, 3, 4)

def avg(fn):
    def wrap(*arg):
        a = ""
        for i in arg:
            a += str(i) + ", "
        print("Среднее Арифметическое чисел:", a[:-2], "=", fn(*arg))

    return wrap


@avg
def summa(*args):
    print("Сумма чисел:", *args, "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)

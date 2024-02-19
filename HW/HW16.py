
def decor(fn):
    def wrap(*args):
        return print("Среднее Арифметическое чисел:", ", ".join(map(str, args)), "=", fn(*args) / len(args))

    return wrap


@decor
def func(*args):
    summa = sum(args)
    print("Сумма чисел:", ", ".join(map(str, args)), "=", summa)
    return summa


func(2, 3, 3, 4)



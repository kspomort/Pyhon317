def num(x):  # n = []
    if not x:
        return 0
    count = 0  # 0
    if x[0] < 0:
        count += 1
    return num(x[1:]) + count  # 1 + 0 + 0 + 1 + 1 + 0 + 0


lst = [-2, 3, 8, -11, -4, 6]
print(num(lst))
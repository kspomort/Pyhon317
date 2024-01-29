num = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
uni = {}
for i in num:
    if i in uni:
        uni[i] += 1
    else:
        uni[i] = 1
print(num)
for i, qty in uni.items():
    print("Количество", i, "=", qty)

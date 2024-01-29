n = int(input("Введите количество копеек: "))
if 0 <= n <= 99:
    print("Вы ввели:", end=" ")
    if n % 10 == 1 and n != 11:
        print(n, "копейка")
    elif 2 <= (n % 10) <= 4 and n != 14 and n != 13 and n != 12:
        print(n, "копейки")
    else:
        print(n, "копеек")

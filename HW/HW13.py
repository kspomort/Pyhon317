students = {}

# def ch(*args):
#     average = sum(args) / len(args)
#     print(average)
#     res = []
#     for num in args:
#         if average < num:
#             res.append(num)
#     return res

qty = int(input("Кол-во студентов: "))
summa = 0
for i, key in enumerate(range(qty), 1):
    name = input(str(i) + "-й студент: ")
    score = int(input("Средний Балл: "))
    students[name] = score
    summa += score

avg_score = summa / qty
print("Средний балл:", avg_score)
for key in students:
    if students[key] > avg_score:
        print("Студенты с баллом выше среднего", key)



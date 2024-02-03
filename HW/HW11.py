math_winners, fis_winners = ['Матвей', 'Евгения', 'Михаил', 'Максим', 'Наталья'], ['Максим', 'Матвей', 'Александр']
unique_winners = list((math_winners + fis_winners))
print("Все призы:", unique_winners)
both_winners = set(math_winners) & set(fis_winners)
print("Призеры обеих олимпиад:", both_winners)
math_winners = set(math_winners) & set(fis_winners)
print("Обновленный список призеров по математике:", math_winners)

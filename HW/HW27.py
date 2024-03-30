c1 = Clock(80000)
print(c1.get_format_time())
c1["hour"] = 11
c1["min"] = 24
c1["sec"] = 59
print(c1["hour"], c1["min"], c1["sec"])
print(c1.get_format_time())

c1 = Clock(100)
c2 = Clock(200)
c4 = Clock(300)
print(c1.get_format_time())
print(c2.get_format_time())
print(c4.get_format_time())
c3 = c1 + c2 + c4
print(c3.get_format_time())
c1 += c2
print(c1.get_format_time())
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")

if c1 != c2:
    print("Время разное")
else:
    print("Время равно")
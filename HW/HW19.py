import re
pattern_password = re.compile(r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.)[0-9a-z!@_-]{8,18}$')
password = input("Введите пароль: ")


def comp(a, b):
    if bool(a.match(b)) is True:
        print("Пароль", b, "- надежный!")
    else:
        print("Пароль не достаточно надежный!")


comp(pattern_password, password)




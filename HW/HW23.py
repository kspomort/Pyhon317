class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        print("Имя удалено.")
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        print("Возраст удален.")
        del self.__age


pr = Person("Ирина", 26)
print(pr.__dict__)
print(pr.name, pr.age)
pr.name = "Игорь"
pr.age = 31
print(pr.__dict__)
print(pr.name, pr.age)
del pr.name
print(pr.__dict__)
class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook

    def print_info(self):
        print(f"{self.name} => {self.notebook.brand}, {self.notebook.proc}, {self.notebook.mem}")

    class Notebook:
        brand = "HP"
        proc = "i7"
        mem = "16"


r = Student("Roman")
r2 = Student("Vladimir")
r.print_info()
r2.print_info()
class Auto:
    model = "model"
    year = "0000"
    firm = "firm"
    capacity = "capacity"
    color = "color"
    price = "price"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели : {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.firm}\nОбъем двигателя: "
              f"{self.capacity}\nЦвет: {self.color}\nЦена: {self.price}")
        print("*" * 40)

    def input_info(self, model, year, firm, capacity, color, price):
        self.model = model
        self.year = year
        self.firm = firm
        self.capacity = capacity
        self.color = color
        self.price = price

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.model = year

    def get_year(self):
        return self.year

    def set_firm(self, firm):
        self.model = firm

    def get_firm(self):
        return self.firm

    def set_capacity(self, capacity):
        self.model = capacity

    def get_capacity(self):
        return self.capacity

    def set_color(self, color):
        self.model = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.model = price

    def get_price(self):
        return self.price


h1 = Auto()
h1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
h1.print_info()


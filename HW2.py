class Vehice:
    __COLOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        pass
    def get_model(self):
        print(f'Модель: {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        j = 0
        for i in self.__COLOR_VARIANT:
            if new_color.upper() in i.upper():
                self.__color = new_color
                j = 1
        if j == 0:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehice):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedor','Toyota Mark II','blue','500')
vehicle1.print_info()
vehicle1.set_color("Pink")
vehicle1.set_color('BLACK')
vehicle1.owner = "Vasyok"
vehicle1.print_info()

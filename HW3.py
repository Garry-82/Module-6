class Vehicle:
    vehicle_type = "none"
class Car:
    price = 1000000
    def __init__(self, name):
        self.name = name
    def horse_powers(self, power):
        print(f' У {self.name}   {power} лошадиных сил')
class Nissan(Car, Vehicle):
    Vehicle.vehicle_type ="машина"
    def __init__(self, name, price, power):
        super().__init__(name)
        Car.price = price
        super().horse_powers(power)



extrail = Nissan('Extrail', 1500000, 300)

print(extrail.vehicle_type)
print(extrail.price)
extrail.horse_powers(500)




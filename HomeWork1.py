class Animal:  # - класс "Животные"
    alive = True  # - атрибут "Живой"
    fed = False  # - атрибут "накормленный"
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        food = food
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True  # - накормлен!!
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False  # - умер от голода
class Plat:  # - класс "Растения"
    edible = False  # - съедобность
    def __init__(self,name):
        self.name = name
class Mammal(Animal):  # - млекопитающие
    pass
class Predator(Animal):  # - хищник
    pass
class Flower(Plat):
    pass
class Fruit(Plat):
    edible = True


a1 = Predator("Волк с Уолл-Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")


print(a1.name)
print(a2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass
        
class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Aeroplane(Vehicle):
    def move(self):
        print("Fly!")
        

car = Car("Tata", "Safari")

boat = Boat("Ibiza", "Touring 20")

aeroplane = Aeroplane("Airbus", "123")

for x in (car, boat, aeroplane):
    print(x.brand, x.model)
    x.move()
class MyClass:
    species = "Humans"

    def __init__(self, name):
        self.name = name


class HumanClass(MyClass):
    def __init__(self, name):
        MyClass.__init__(self, name)

a = HumanClass("Arav")

print(a.name)
print(a.species)

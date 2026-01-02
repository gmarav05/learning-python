class MyClass:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return(f"Hello {self.name}, Welcome to my program!")



a = MyClass("Arav")
print(a.greeting())
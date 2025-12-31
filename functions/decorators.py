def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def my_function():
    return "Hello Decorator"

print(my_function())
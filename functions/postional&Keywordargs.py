def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 20, d = 89)
print(result)
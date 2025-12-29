x = ("Apple", "banana")
y = list(x)
y[1] = "mango"
y.append("Kiwi")
x = tuple(y)

print(x)


y = list(x)
y.remove("Apple")
x = tuple(y)
print(x)
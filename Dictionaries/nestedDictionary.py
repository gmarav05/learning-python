myFood = {
    "Item1" : {
        "name":"Paneer",
        "price":"Expensive"
    },
    "Item2" : {
        "name":"Potato",
        "price":"affordable"
    }
}

# print(myFood.items())

# print(myFood["Item2"]["price"])


for x,obj in myFood.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
    
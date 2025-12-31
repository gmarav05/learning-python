
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name", myvar["name"])
  print("age", myvar["age"])
  print("city", myvar["city"])


my_function(name = "Tobias", age = 30, city = "Bergen")

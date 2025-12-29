thisset = {"apple", "banana", "cherry"}
thisset.add("watermelon")
tropical = {"pineapple", "mango", "papaya"}
myList = ["Kiwi"]
thisset.update(myList)
thisset.update(tropical)

for x in thisset:
    print(x)

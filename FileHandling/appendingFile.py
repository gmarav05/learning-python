with open("demofile.txt", 'a') as f:
    print(f.write("\nThis is my first file handling in python!"))

with open("demofile.txt", 'r') as f:
    print(f.read())

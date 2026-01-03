with open("newFile.txt", 'x') as f:
    f.write("This file is created using 'x' \n which is used to create file.")

with open("newFile.txt", 'r') as f:
    print(f.read())

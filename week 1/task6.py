with open("data.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

print("The file has been created.\n")

print("The content of the file:")
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
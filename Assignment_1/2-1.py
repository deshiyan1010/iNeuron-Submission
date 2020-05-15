string = input("Enter comma seperated entry: ")

lst = string.split(",")

list_int = [int(x) for x in lst ]
print(list_int)

print("test")
max = None
list = [1, 2, 3, 44, 4, 5, 6, 99, 4, 5, 6]
for number in list:
    if max < number:
        max = number
    print(max)
print(max)
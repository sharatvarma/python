def binarySearch():
    names = ["sharat", "varma", "chandra", "pakalapati", "murthy", "Venky",
             "dan", "visu", "ram", "harish"]
    names.sort()
    name = input('What name are you looking for : ')
    lower_bound = 0
    upper_bound = len(names) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound) // 2
        if name > names[middle_pos]:
            lower_bound = middle_pos + 1
        elif name < names[middle_pos]:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("The name is at position", middle_pos, names)
    else:
        print("The name was not in the list.")

print(binarySearch())
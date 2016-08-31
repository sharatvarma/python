def binarySearch():
    names = ["Sharat", "varma", "chandra", "pakalapati", "murthy", "Venky",
             "dan", "visu", "ram", "harish"]
    names.sort()
    name = input('What name are you looking for : ')
    lower_bound = 0
    upper_bound = len(names) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound+upper_bound) // 2
        if names[middle_pos] < name:
            lower_bound = middle_pos + 1
        elif names[middle_pos] > name:
            upper_bound = middle_pos - 1
        else:
            found = True

    if found:
        print("The name is at position", middle_pos)
    else:
        print("The name was not in the list.")

print(binarySearch())
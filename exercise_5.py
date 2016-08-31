
'''
def fermat_last():
    n1 = int(input("Enter a: "))
    n2 = int(input("Enter b: "))
    n3 = int(input("Enter c: "))
    factor = int(input("Enter n: "))
    num1 = math.pow(n1, factor)
    num2 = math.pow(n2, factor)
    num3 = math.pow(n3, factor)
    sum = num1 + num2
    if factor >= 2:
        if sum == num3:
            print("Fermat is wrong")
        else:
            print("No, that doesn’t work")

print(fermat_last())
'''

'''
def is_triangle():
    l1 = int(input("Enter l1: "))
    l2 = int(input("Enter l2: "))
    l3 = int(input("Enter l3: "))
    if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
        print("Cannot form triangle")
    else:
        print("Forms triangle")

is_triangle()
'''


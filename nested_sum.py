'''
#10.6
def is_sorted(list1=[]):
    for i in list1:
        if list1[i] < list1[i+1]:
            return True
        elif list1[i] > list1[i+1]:
            return False
        else:
            print("Pass the parameters in the list")

result = is_sorted([3, 2, 3])
print(result)
'''
# 10.8 -- 1
'''
s = ['sharat', 'sharat', 'sharat', 'kumar']
for i in s:
    if s.count(i) > 1:
        print(i, 'duplicate')
    else:
        print('No duplicate')

'''

'''10.11
def bisect():
    list1 = [1, 2, 3, 4]
    input_num = int(input("Enter the target value: "))
    for i,n in enumerate(list1):
        if input_num == list1[i]:
            print(list1.index(input_num), '- is the index value ')
        else:
            print('No value matched')

bisect()'''

''' 10.10
def read_write():

    fw = open('word.txt', 'w')
    fw.write('Hello sharat varma')
    fw.close()

    fr = open('word.txt', 'r')
    text = fr.read()
    list1 = []

    text2 = text.split(" ")
    list1.append(text2)
    print(list1)

read_write()'''


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





# left -- 10.7 ,10.8(2),10.9,10.12,12.13
#
# Done -- 10.6,10.8(1),10.10,10.11

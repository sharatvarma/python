'''11.1
def dictionary():
    fw = open('dict.txt', 'w')
    fw.write('Sharat varma')
    fw.close()

    fr = open('dict.txt', 'r')
    text = fr.read()
    d = dict()
    text2 = text.split()
    for i, n in enumerate(text2):
        d[n] = i
        print(d)

dictionary()
#print(res)
'''



'''
11.2
a = {1: 'sharat', 2: 'varma'}
k = int(input("Enter the key :"))
if k in a:
    print(a[k])
else:
    print(a.get(k, "No value for the key"))
'''

'''
11.10
letter = 'Cheer'
value = 7
word_list = ''
for i in letter:
    new = ord(i)
    new += value
    nice_char = chr(new)
    print(i, '=>', nice_char)

    for x in nice_char:
        word_list += x
        print(word_list)
'''













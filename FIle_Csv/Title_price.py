import csv


def title_price():
    fr = open("100books.csv", 'r')
    reader = csv.DictReader(fr)

    for lines in reader:
        print(lines['title'] + "-->" + lines['price'])

title_price()

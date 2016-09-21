import csv

def rs_to_usd():
    fr = open("100books.csv", 'r')
    reader = csv.reader(fr)

    fw = open("100books_pipe.csv", 'w')
    writer = csv.DictWriter(fw, fieldnames=)


rs_to_usd()
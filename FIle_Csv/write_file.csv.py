import csv

def details():
    while True:
        a = input("Enter Y to add new book details else N to exit [Y/N]: ")
        if a == "Y":
            title = input("Enter the title name: ")
            author = input("Enter the author name: ")
            price = int(input("Enter the price of the book: "))
            fieldnames = ['book_id', 'title', 'authors', 'binding', 'pages', 'price', 'isbn', 'image_url']

            fw = open("100books.csv", 'a')
            writer = csv.DictWriter(fw, delimiter=",", restval='none', fieldnames=fieldnames)
            writer.writerow({'title': title, 'authors': author, 'price': price})
        elif a == 'N':
            break
        else:
            print("Either Y or N")

details()


#How to append in the new line

import csv

def add_book():
    try:
        name = input("Name: ")
        author = input("Author: ")
        price = int(input("Price: "))
        date = input("Date: ")
        status = 'A'

        with open('books.csv', 'a', newline='') as f1:
            b = csv.writer(f1)
            b.writerow([name, author, price, date, status])

    except ValueError:
        print("Invalid price format. Please enter a valid integer price.")
    except Exception as e:
        print("An error occurred:", e)

def display_books():
    try:
        books_data = []
        with open('books.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                books_data.append(row)
        return books_data
    except FileNotFoundError:
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def search_book_by_name(book_name):
    try:
        with open('books.csv', 'r', newline='') as csvfile:
            found = False
            for line in csvfile:
                fields = line.strip().split(',')
                if fields[0].lower() == book_name.lower():
                    found = True
                    print("Yes, this book is available in records.")
                    break
            if not found:
                print("Book not found in records.")
    except FileNotFoundError:
        print("File 'books.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)

def remove_book_by_name(book_name):
    try:
        temp_books = []
        with open('books.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            found = False
            for row in reader:
                if row[0].lower() == book_name.lower():
                    found = True
                else:
                    temp_books.append(row)
        
        if found:
            with open('books.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(temp_books)
            print("Book removed successfully.")
        else:
            print("Book not found in records.")
    except FileNotFoundError:
        print("File 'books.csv' not found.")
    except Exception as e:
        print("An error occurred:", e)

def issue_book(book_name):
   
    temp_books = []
    found = False 
    with open('books.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == book_name.lower():
                if row[4] == 'A':
                    row[4] = 'I' 
                    found = True
                else:
                    print("Book already issued.")
            temp_books.append(row)

    if found:
        with open('books.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(temp_books)
            raise Exception
    elif not found:
        raise ValueError

def return_book(book_name):
  
    temp_books = []
    found = False
    with open('books.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0].lower() == book_name.lower():
                if row[4] == 'I': 
                    row[4] = 'A'
                    found = True
                else:
                    print("Book already available.")
            temp_books.append(row)

    if found:
        with open('books.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(temp_books)
            raise Exception
    elif not found:
        raise ValueError 



from tkinter import*
from tkinter import messagebox
from tkinter import Tk, Button, Label
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import booksys
import membersys
import csv
import pandas as pd
"""
display_csv_details #this function is used for displayin the deatails of members and books in a csv file

add_member          #functions that are used for performing different tasks in the Library 
search_member
add_book
search_book
remove_book_window
remove_member_window
issue_book
return_book

display_books_window    #these are the windows that displays the records
display_members_window


main_window          #these are the different gui windows
booksgui
membergui  
    

"""
def display_csv_details(csv_file):
    df = pd.read_csv(csv_file)

    root = tk.Tk()
    root.title("Books Details")

    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)

    for column in df.columns:
        tree.heading(column, text=column)

    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

    scroll_y = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    scroll_y.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scroll_y.set)

    tree.pack(expand=True, fill="both")
    
    root.mainloop()

def add_member():
    def add_member_to_csv():
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

        try:
            with open('members.csv', 'a', newline='') as f1:
                b = csv.writer(f1)
                b.writerow([name, email, phone])
                messagebox.showinfo("Success", "Member added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
 
    add_window = Toplevel()
    add_window.title("Add a Member")
    add_window.config(padx=50, pady=20)

    name_label = Label(add_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1)

    email_label = Label(add_window, text="Email:")
    email_label.grid(row=1, column=0)
    email_entry = Entry(add_window)
    email_entry.grid(row=1, column=1)

    phone_label = Label(add_window, text="Phone:")
    phone_label.grid(row=2, column=0)
    phone_entry = Entry(add_window)
    phone_entry.grid(row=2, column=1)

    add_button = Button(add_window, text="Add", command=add_member_to_csv)
    add_button.grid(row=3, column=0, columnspan=2)

def search_member():
    def search_member_in_csv():
        member_name = search_entry.get()
        try:
            with open('members.csv', 'r', newline='') as csvfile:
                found = False
                for line in csvfile:
                    fields = line.strip().split(',')
                    if fields[0].lower() == member_name.lower():
                        found = True
                        messagebox.showinfo("Result", "Yes, this member exists in the records.")
                        break
                if not found:
                    messagebox.showinfo("Result", "Member not found in records.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'members.csv' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    search_window = Toplevel()
    search_window.title("Search a Member")
    search_window.config(padx=50, pady=20)

    search_label = Label(search_window, text="Enter the name of the member:")
    search_label.pack()

    search_entry = Entry(search_window)
    search_entry.pack()

    search_button = Button(search_window, text="Search", command=search_member_in_csv)
    search_button.pack()

def add_book():
    def add_book_to_csv():
        name = name_entry.get()
        author = author_entry.get()
        price = price_entry.get()
        date = date_entry.get()
        status = 'A'

        try:
            price = int(price)
            with open('books.csv', 'a', newline='') as f1:
                b = csv.writer(f1)
                b.writerow([name, author, price, date, status])
                messagebox.showinfo("Success", "Book added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid price format. Please enter a valid integer price.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    add_window = Toplevel()
    add_window.title("Add a Book")
    add_window.config(padx=50, pady=20)

    name_label = Label(add_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = Entry(add_window)
    name_entry.grid(row=0, column=1)

    author_label = Label(add_window, text="Author:")
    author_label.grid(row=1, column=0)
    author_entry = Entry(add_window)
    author_entry.grid(row=1, column=1)

    price_label = Label(add_window, text="Price:")
    price_label.grid(row=2, column=0)
    price_entry = Entry(add_window)
    price_entry.grid(row=2, column=1)

    date_label = Label(add_window, text="Date:")
    date_label.grid(row=3, column=0)
    date_entry = Entry(add_window)
    date_entry.grid(row=3, column=1)

    add_button = Button(add_window, text="Add", command=add_book_to_csv)
    add_button.grid(row=4, column=0, columnspan=2)

def search_book():
    def search_book_in_csv():
        book_name = search_entry.get()
        try:
            with open('books.csv', 'r', newline='') as csvfile:
                found = False
                for line in csvfile:
                    fields = line.strip().split(',')
                    if fields[0].lower() == book_name.lower():
                        found = True
                        messagebox.showinfo("Result", "Yes, this book is available in records.")
                        break
                if not found:
                    messagebox.showinfo("Result", "Book not found in records.")
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'books.csv' not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    search_window = Toplevel()
    search_window.title("Search a Book")
    search_window.config(padx=50, pady=20)

    search_label = Label(search_window, text="Enter the name of the book:")
    search_label.pack()

    search_entry = Entry(search_window)
    search_entry.pack()

    search_button = Button(search_window, text="Search", command=search_book_in_csv)
    search_button.pack()

def remove_book_window():
    
    def remove_book():
        book_name = entry.get()
        remove_result = booksys.remove_book_by_name(book_name)
        if remove_result:
            pass
        else:
            messagebox.showinfo("Success", "Book removed successfully.")

    window = Toplevel()
    window.title("Remove a Book")
    window.config(padx=50, pady=20)

    label = Label(window, text="Enter the name of the book:")
    label.pack()

    entry = Entry(window)
    entry.pack()

    remove_button = Button(window, text="Remove", command=remove_book)
    remove_button.pack()

def remove_member_window():
    
    def remove_member():
        member_name = entry.get()
        remove_result = membersys.remove_member_by_name(member_name)
        messagebox.showinfo("Success", "Member removed successfully..")

    window = Toplevel()
    window.title("Remove a Member")
    window.config(padx=50, pady=20)

    label = Label(window, text="Enter the name of the member:")
    label.pack()

    entry = Entry(window)
    entry.pack()

    remove_button = Button(window, text="Remove", command=remove_member)
    remove_button.pack()
    
def display_members_window():
    csv_file_path = "members.csv"
    display_csv_details(csv_file_path)
        
def issue_book():
    
    def issue_book_from_csv():
        book_name = issue_entry.get()
        try:
            booksys.issue_book(book_name)
        except ValueError :
            messagebox.showerror("Error", "An error occurred: ")
        except Exception:
            messagebox.showinfo("Success",'The book is Issued')

    issue_window = Toplevel()
    issue_window.title("Issue a Book")
    issue_window.config(padx=50, pady=20)

    issue_label = Label(issue_window, text="Enter the name of the book to issue:")
    issue_label.pack()

    issue_entry = Entry(issue_window)
    issue_entry.pack()

    issue_button = Button(issue_window, text="Issue", command=issue_book_from_csv)
    issue_button.pack()
    
def return_book():
    def return_book_to_csv():
        book_name = return_entry.get()
        try:
            booksys.return_book(book_name)
        except ValueError :
            messagebox.showerror("Error", "An error occurred: ")
        except Exception:
            messagebox.showinfo("Success",'The book is Returned')

    return_window = Toplevel()
    return_window.title("Return a Book")
    return_window.config(padx=50, pady=20)

    return_label = Label(return_window, text="Enter the name of the book to return:")
    return_label.pack()

    return_entry = Entry(return_window)
    return_entry.pack()

    return_button = Button(return_window, text="Return", command=return_book_to_csv)
    return_button.pack()


def display_books_window():
    
    csv_file_path = "books.csv"
    display_csv_details(csv_file_path)

def main_window():
    
    global window
    window = Tk()
    window.config(padx=100, pady=50)
    window.configure()

    def handel():
        window.destroy()
    f = font.Font(size=10, weight="bold",family='Arial')
    fheading = font.Font(size=15, weight="bold",family='Arial')
    l1=Label(text="LIBRARY MANAGEMENT SYSTEM", font=fheading,bg="white", fg="blue")
    
    button1 = Button(text="Members", command=membergui,bg="cyan" ,height = 2,width=20, fg= "black",font=f)
    button2 = Button(text="Books", command=booksgui,bg="cyan" ,height = 2,width=20, fg= "black",font=f)
    button3 = Button(text="Return", command=return_book,bg="cyan" ,height = 2,width=20, fg= "black",font=f)
    button4 = Button(text="Issue", command=issue_book,bg="cyan" ,height = 2,width=20, fg= "black",font=f)
    button5 = Button(text="Exit",command=handel,bg="cyan",height = 2,width=20, fg= "black",font=f)
 
    l1.grid(row=0,column=0 ,padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    button1.grid(row=1, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    button2.grid(row=2, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    button3.grid(row=3, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    button4.grid(row=4, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    button5.grid(row=5, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)

    
    window.mainloop()

def booksgui():
     
    window.destroy()
    window3=Tk()
    window3.configure()    
    
    def handel():
        window3.destroy()

    def home():
        window3.destroy()
        main_window()
    
    def remove_book_handel():
        remove_book_window()
        
    window3.title("Book window Menu")
    window3.config(padx=100, pady=50)
   
    f = font.Font(size=10, weight="bold",family='Arial')
    fheading = font.Font(size=15, weight="bold",family='Arial')
    
    l1=Label(text="BOOK WINDOW", font=fheading,bg="white", fg="blue")
    b1 = Button(text="Add Book", command=add_book,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b2 = Button(text="Search Book", command=search_book,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b3 = Button(text="Display books", command=display_books_window,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b4 = Button(text="Remove a book", command=remove_book_handel,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b5 = Button(text="Cancel", command=handel,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b6 = Button(text="Home", command=home,bg="cyan",height = 2,width=20, fg= "black",font=f)
    
    l1.grid(row=0,column=1 ,padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b1.grid(row=1, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b2.grid(row=2, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b3.grid(row=3, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b4.grid(row=4, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b5.grid(row=7, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b6.grid(row=7, column=3, padx=10, pady=10, sticky="n", ipadx=20, ipady=10) 
    window3.mainloop()

def membergui():
    global window
    window.destroy()
    window2 = Tk()
    window2.configure()
    
    def handle_cancel():
        window2.destroy()
        
    def home():
        window2.destroy()
        main_window()
    
    window2.title("Member window Menu")
    window2.config(padx=100, pady=50)
    f = font.Font(size=10, weight="bold",family='Arial')
    fheading = font.Font(size=15, weight="bold",family='Arial')       
    
    l1=Label(text="MEMBER WINDOW" ,font=fheading,bg="white", fg="blue")
    b1 = Button(text="Add Member", command=add_member,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b2 = Button(text="Search Member", command=search_member,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b3 = Button(text="Display members", command=display_members_window,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b4 = Button(text="Remove a member", command=remove_member_window,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b5 = Button(text="Cancel", command=handle_cancel,bg="cyan",height = 2,width=20, fg= "black",font=f)
    b6 = Button(text="Home",command=home,bg="cyan",height = 2,width=20, fg= "black",font=f)

    l1.grid(row=0,column=1 ,padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b1.grid(row=1, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b2.grid(row=2, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b3.grid(row=3, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b4.grid(row=4, column=1, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b5.grid(row=7, column=0, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)
    b6.grid(row=7, column=3, padx=10, pady=10, sticky="n", ipadx=20, ipady=10)      

    window2.mainloop()

main_window()



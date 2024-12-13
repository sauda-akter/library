import json
from datetime import datetime, timedelta
import save_all_books

def lend_books(all_books):
    borrower_name = input("Enter borrower's name: ")
    phone_number = input("Enter borrower's phone number: ")
    book_title = input("Enter book title: ")
    return_date = datetime.now() + timedelta(days = 14)
    return_date_str = return_date.strftime("%Y-%m-%d")

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                lends = restore_lends()
                lends[borrower_name] = {
                    "phone_number": phone_number,
                    "book_title": book_title,
                    "return_date": return_date_str
                }
                save_lends(lends)
                save_all_books.save_all_books(all_books)
                print(f"Book lent successfully! Return by {return_date_str}.")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books
    print("Book not found in the inventory.")
    return all_books

def restore_lends():
    try:
        with open('lends.json', 'r') as fp:
            lends = json.load(fp)
    except FileNotFoundError:
        lends = {}
    return lends

def save_lends(lends):
    with open('lends.json', 'w') as fp:
        json.dump(lends, fp, indent = 4)

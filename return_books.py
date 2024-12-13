import json
import save_all_books

def return_books(all_books):
    borrower_name = input("Enter borrower's name: ")

    lends = restore_lends()
    if borrower_name in lends:
        book_title = lends[borrower_name]['book_title']
        for book in all_books:
            if book["title"].lower() == book_title.lower():
                book["quantity"] += 1
                del lends[borrower_name]
                save_lends(lends)
                save_all_books.save_all_books(all_books)
                print("Book returned successfully!")
                return all_books
    print("Borrower information not found.")
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
        json.dump(lends, fp, indent=4)

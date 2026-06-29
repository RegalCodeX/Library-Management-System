def add_book():
    f = open("books.txt", "a")
    b_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    f.write(b_id + "|" + name + "|" + author + "|Available\n")
    f.close()
    print("Book added successfully")


def display_books():
    f = open("books.txt", "r")
    print("BookID | Book Name | Author | Status")
    for line in f:
        print(line.strip())
    f.close()


def search_book():
    f = open("books.txt", "r")
    b_id = input("Enter Book ID to search: ")
    found = False

    for line in f:
        if line.startswith(b_id):
            print("Book Found:", line)
            found = True

    if not found:
        print("Book not found")

    f.close()


def issue_book():
    b_id = input("Enter Book ID to issue: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        if line.startswith(b_id) and "Available" in line:
            line = line.replace("Available", "Issued")
            print("Book issued successfully")
        f.write(line)

    f.close()


def return_book():
    b_id = input("Enter Book ID to return: ")

    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in lines:
        if line.startswith(b_id) and "Issued" in line:
            line = line.replace("Issued", "Available")
            print("Book returned successfully")
        f.write(line)

    f.close()


while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        add_book()
    elif ch == '2':
        display_books()
    elif ch == '3':
        search_book()
    elif ch == '4':
        issue_book()
    elif ch == '5':
        return_book()
    elif ch == '6':
        print("Thank you")
        break
    else:
        print("Invalid choice")

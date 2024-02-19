class Library:
    def __init__(self):
        self.file = open("books.txt", "a+", encoding="utf-8")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        for line in lines:
            book_info = line.split(',')
            print(f"Book Name: {book_info[0]}, Author: {book_info[1]}, Release Date: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release date: ")
        num_pages = input("Enter the number of pages: ")

        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self, title):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        new_lines = []
        for line in lines:
            if title not in line:
                new_lines.append(line)
        self.file.seek(0)
        self.file.truncate()
        for new_line in new_lines:
            self.file.write(new_line + '\n')

        print("Book removed successfully.")


lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        title_to_remove = input("Enter the title of the book to remove: ")
        lib.remove_book(title_to_remove)
    else:
        print("Invalid choice. Please try again.")

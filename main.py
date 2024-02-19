class Library:
    def __init__(self):#yapıcı metodumuz
        self.file = open("books.txt", "a+")#books adında txt(database) oluşturduk.

    def __del__(self):
        self.file.close()

    def list_books(self):# kitapları listeleyeceğimiz fonksiyon.
        self.file.seek(0)# dosya içerisinde başlangıça götürür.
        books = self.file.readlines()#dosya okuma
        for book in books:
            book_info = book.strip().split(",")#her veriyi sonunda , ile birlikte liste içerisinde tutar.
            print(f"Book Name: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)#txt dosyasına veri ekler.
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]#silinecek veri dışındaki verileri update listesinde.
        self.file.seek(0)
        self.file.truncate()#txt dosyasındaki tüm verileri temizler
        self.file.writelines(updated_books)#dosyaya silinen veri dışındaki verileri ekler.
        print("Book removed.")


lib = Library()


while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice = input("Enter your choice (1-3 or q): ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        quit()
    else:
        print("Invalid choice.")




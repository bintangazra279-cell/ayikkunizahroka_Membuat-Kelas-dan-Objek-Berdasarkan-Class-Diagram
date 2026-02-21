from datetime import datetime
class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = None
        self.returned = False

    def borrow_book(self, book, staff):
        if not book.is_borrowed:
            book.borrow()
            self.borrow_date = datetime.now().strftime("%Y-%m-%d")
            self.returned = False
            self.member.borrowed_books.append(self)
            print(f"{self.member.name} berhasil meminjam {book.title}")
        else:
            print("Buku sedang tidak tersedia")

    def return_book(self, book, staff):
        if not self.returned:
            book.return_book()
            self.returned = True
            from datetime import datetime
class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = None
        self.returned = False

    def borrow_book(self, book, staff):
        if not book.is_borrowed:
            book.borrow()
            self.borrow_date = datetime.now().strftime("%Y-%m-%d")
            self.returned = False
            self.member.borrowed_books.append(self)
            print(f"{self.member.name} berhasil meminjam {book.title} dilayani oleh {staff.name}")
        else:
            print("Buku sedang tidak tersedia")

    def return_book(self, book, staff):
        if not self.returned:
            book.return_book()
            self.returned = True
            print(f"{self.member.name} mengembalikan {book.title} kepada {staff.name}")
        else:
            print("Buku sudah dikembalikan")
        else:

            print("Buku sudah dikembalikan")

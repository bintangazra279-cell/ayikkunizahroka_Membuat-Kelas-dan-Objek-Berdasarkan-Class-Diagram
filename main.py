from book import Book
from member import Member
from staff import Staff
from BorrowTransaction import BorrowTransaction


if __name__ == "__main__":
    print("===== SISTEM PEMINJAMAN PERPUSTAKAAN =====")

    # Membuat objek buku
    book1 = Book("Python OOP", "Budi", "ISBN001")
    book2 = Book("Struktur Data", "Andi", "ISBN002")
    daftar_buku = [book1, book2]

    # Membuat objek member
    member1 = Member("Ayik", "M001")
    member2 = Member("langit", "M002")
    daftar_member = [member1, member2]

    # Membuat objek staff
    staff1 = Staff("Rina", "S001")

    # MENAMPILKAN DAFTAR BUKU AWAL
    print("\n===== DAFTAR BUKU =====")
    for b in daftar_buku:
        status = "Dipinjam" if b.is_borrowed else "Tersedia"
        print(f"{b.title} | {b.author} | Status: {status}")

    # TRANSAKSI PEMINJAMAN
    print("\n--- Transaksi Peminjaman 1 ---")
    transaksi1 = BorrowTransaction(book1, member1, staff1)
    transaksi1.borrow_book(book1, staff1)

    # MENAMPILKAN STATUS BUKU SETELAH DIPINJAM
    print("\n===== STATUS BUKU SETELAH PEMINJAMAN =====")
    for b in daftar_buku:
        status = "Dipinjam" if b.is_borrowed else "Tersedia"
        print(f"{b.title} | Status: {status}")

    # PENGEMBALIAN
    print("\n--- Pengembalian Buku ---")
    transaksi1.return_book(book1, staff1)

    # MENAMPILKAN STATUS AKHIR
    print("\n===== STATUS AKHIR BUKU =====")
    for b in daftar_buku:
        status = "Dipinjam" if b.is_borrowed else "Tersedia"
        print(f"{b.title} | Status: {status}")

    # RIWAYAT MEMBER
    print("\n===== RIWAYAT PEMINJAMAN MEMBER =====")
    for t in member1.borrowed_books:
        print(f"{member1.name} meminjam {t.book.title} pada {t.borrow_date}")

    print("\n===== PROGRAM SELESAI =====")
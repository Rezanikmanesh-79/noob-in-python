from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sql  
import datetime


icon_address = r"C:\Users\rezan\Desktop\python\project\icon.ico"

def main():
    window = Tk()
    window.title("Booker")
    window.minsize(1080, 720)
    window.iconbitmap(icon_address)

    Label(window, text="Reza Nikmanesh", font=("", 18)).pack()
    
    Label(window, text="Username:").pack()
    username_entry = Entry(window)
    username_entry.pack()

    Label(window, text="Password:").pack()
    password_entry = Entry(window, show="*")
    password_entry.pack()

    status_label = Label(window, text="", font=("", 14))
    status_label.pack()

    Button(window, text="Login", bg="red", fg="white", 
           command=lambda: login(username_entry.get(), password_entry.get(), status_label, window)).pack()

    window.mainloop()

def login(username, password, status_label, window):
    if username == "admin" and password == "1234":
        status_label.config(text="You are logged in!", fg="green")
        window.after(1000, lambda: open_library_window(window))
    else:
        status_label.config(text="Incorrect username or password.", fg="red")

def open_library_window(window):
    window.withdraw()  # پنهان کردن پنجره جاری
    main_window = Toplevel()  # ایجاد پنجره جدید
    main_window.title("Library Management")
    main_window.iconbitmap(icon_address)
    main_window.minsize(1080, 720)
    
    Label(main_window, text="Welcome to the Library Management System!", font=("", 18)).pack()
    
    Button(main_window, text="Management of books", bg="blue", fg="white", command=lambda: Management_of_books(main_window)).pack(pady=10)
    Button(main_window, text="Member management", bg="blue", fg="white", command=lambda: Member_management(main_window)).pack(pady=10)
    Button(main_window, text="Staff management", bg="blue", fg="white", command=lambda: Staff_management(main_window)).pack(pady=10)
    Button(main_window, text="Deposit management", bg="blue", fg="white", command=lambda: Deposit_management(main_window)).pack(pady=10)
    Button(main_window, text="Logout", bg="red", fg="white", command=main_window.destroy).pack(pady=10)

# مدیریت کتاب‌ها
def Management_of_books(main_window):
    main_window.withdraw()
    books_window = Toplevel()
    books_window.title("Library Management")
    books_window.iconbitmap(icon_address)
    books_window.minsize(1080, 720)
    
    tab_control = ttk.Notebook(books_window)
    
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text="Add New Books")
    tab_control.add(tab2, text="Show/Delete/Edit Books")
    tab_control.pack(expand=1, fill="both")
    
    # --- Tab 1: Add New Book ---
    Label(tab1, text="Add new", font=("", 18)).pack()
    Label(tab1, text="Name of Book:").pack()
    name_book = Entry(tab1)
    name_book.pack()
    Label(tab1, text="Author:").pack()
    author = Entry(tab1)
    author.pack()
    Label(tab1, text="Translator:").pack()
    translator = Entry(tab1)
    translator.pack()
    Label(tab1, text="Subject:").pack()
    subject = Entry(tab1)
    subject.pack()
    Label(tab1, text="Publisher:").pack()
    publisher = Entry(tab1)
    publisher.pack()
    Label(tab1, text="Price:").pack()
    price = Entry(tab1)
    price.pack()

    def submit_book():
        if name_book.get() and author.get() and price.get().isdigit():
            sql.add_book(name_book.get(), author.get(), translator.get(), subject.get(), publisher.get(), float(price.get()))
            messagebox.showinfo("Success", "Book has been added successfully!")
        else:
            messagebox.showerror("Error", "Please fill all required fields with valid data.")
        books_window.destroy()
        Management_of_books(Toplevel())

    Button(tab1, text="Submit", bg="green", fg="white", command=submit_book).pack()

    # --- Tab 2: Show/Delete/Edit Books ---
    Label(tab2, text="List of Books", font=("", 18)).pack(pady=10)
    
    books = sql.get_books()
    for book in books:
        book_info = f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Translator: {book[3]}, Subject: {book[4]}, Publisher: {book[5]}, Price: {book[6]}"
        Label(tab2, text=book_info).pack()
        
        # افزودن دکمه ویرایش به هر کتاب
        Button(tab2, text="Edit", command=lambda b=book: open_edit_book_window(b)).pack()

    Label(tab2, text="Enter Book ID to Delete:").pack(pady=(10, 0))
    book_id_entry = Entry(tab2)
    book_id_entry.pack(pady=(0, 10))

    def delete_book():
        if book_id_entry.get().isdigit():
            success = sql.delete_book(int(book_id_entry.get()))
            if success:
                messagebox.showinfo("Success", "Book has been deleted successfully!")
            else:
                messagebox.showerror("Error", "Book not found.")
        else:
            messagebox.showerror("Error", "Invalid Book ID.")
        books_window.destroy()
        Management_of_books(Toplevel())

    Button(tab2, text="Delete Book", bg="red", fg="white", command=delete_book).pack()

    Button(books_window, text="Back", bg="red", fg="white", command=lambda: open_library_window(books_window)).pack(pady=20)

def open_edit_book_window(book):
    edit_window = Toplevel()
    edit_window.title("Edit Book")
    edit_window.minsize(400, 300)
    
    Label(edit_window, text="Edit Book", font=("", 18)).pack()
    
    Label(edit_window, text="Name of Book:").pack()
    name_book = Entry(edit_window)
    name_book.insert(0, book[1])  # قرار دادن نام کتاب
    name_book.pack()
    
    Label(edit_window, text="Author:").pack()
    author = Entry(edit_window)
    author.insert(0, book[2])  # قرار دادن نویسنده
    author.pack()
    
    Label(edit_window, text="Translator:").pack()
    translator = Entry(edit_window)
    translator.insert(0, book[3])  # قرار دادن مترجم
    translator.pack()
    
    Label(edit_window, text="Subject:").pack()
    subject = Entry(edit_window)
    subject.insert(0, book[4])  # قرار دادن موضوع
    subject.pack()
    
    Label(edit_window, text="Publisher:").pack()
    publisher = Entry(edit_window)
    publisher.insert(0, book[5])  # قرار دادن ناشر
    publisher.pack()
    
    Label(edit_window, text="Price:").pack()
    price = Entry(edit_window)
    price.insert(0, str(book[6]))  # تبدیل قیمت به رشته و قرار دادن آن
    price.pack()

    Button(edit_window, text="Save Changes", bg="green", fg="white", 
           command=lambda: save_book_changes(book[0], name_book.get(), author.get(), translator.get(), subject.get(), publisher.get(), price.get())).pack()

def save_book_changes(book_id, title, author, translator, subject, publisher, price):
    if title and author and price.isdigit():
        sql.update_book(book_id, title, author, translator, subject, publisher, float(price))
        messagebox.showinfo("Success", "Book updated successfully!")
    else:
        messagebox.showerror("Error", "Please fill all required fields with valid data.")

# مدیریت اعضا
def Member_management(main_window):
    def open_edit_member_window(member):
        edit_window = Toplevel()
        edit_window.title("Edit Member")
        edit_window.minsize(400, 300)
        Label(edit_window, text="Edit Member", font=("", 18)).pack()
        name_entry = Entry(edit_window)
        name_entry.insert(0, member[1])
        name_entry.pack()
        national_id_entry = Entry(edit_window)
        national_id_entry.insert(0, member[2])
        national_id_entry.pack()
        phone_entry = Entry(edit_window)
        phone_entry.insert(0, member[3])
        phone_entry.pack()
        address_entry = Entry(edit_window)
        address_entry.insert(0, member[4])
        address_entry.pack()
        Button(edit_window, text="Save", command=lambda: sql.update_member(member[0], name_entry.get(), national_id_entry.get(), phone_entry.get(), address_entry.get())).pack()
    main_window.withdraw()
    Member_window = Toplevel()
    Member_window.iconbitmap(icon_address)
    Member_window.title("Library Management")
    Member_window.minsize(1080, 720)
    
    tab_control = ttk.Notebook(Member_window)
    
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text="Members Management")
    tab_control.add(tab2, text="Show/Delete/Edit Members")
    tab_control.pack(expand=1, fill="both")
    
    # --- Tab 1: Add Member ---
    Label(tab1, text="Members Management", font=("", 18)).pack(pady=10)
    Label(tab1, text="Member Name:").pack()
    member_name_entry = Entry(tab1)
    member_name_entry.pack()
    Label(tab1, text="National ID:").pack()
    national_id_entry = Entry(tab1)
    national_id_entry.pack()
    Label(tab1, text="Phone Number:").pack()
    phone_number_entry = Entry(tab1)
    phone_number_entry.pack()
    Label(tab1, text="Address:").pack()
    address_entry = Entry(tab1)
    address_entry.pack()

    def submit_member():
        if member_name_entry.get() and national_id_entry.get():
            sql.add_member(member_name_entry.get(), national_id_entry.get(), phone_number_entry.get(), address_entry.get())
            messagebox.showinfo("Success", "Member has been added successfully!")
        else:
            messagebox.showerror("Error", "Please fill all required fields.")
        Member_window.destroy()
        Member_management(Toplevel())

    Button(tab1, text="Submit", bg="green", fg="white", command=submit_member).pack(pady=10)

    # --- Tab 2: Show/Delete/Edit Members ---
    Label(tab2, text="List of Members", font=("", 18)).pack(pady=10)

    members = sql.get_members()
    for member in members:
        member_info = f"ID: {member[0]}, Name: {member[1]}, National ID: {member[2]}, Phone: {member[3]}"
        Label(tab2, text=member_info).pack()

        # افزودن دکمه ویرایش به هر عضو
        Button(tab2, text="Edit", command=lambda m=member: open_edit_member_window(m)).pack()

    Label(tab2, text="Enter Member ID to Delete:").pack(pady=(10, 0))
    member_id_entry = Entry(tab2)
    member_id_entry.pack(pady=(0, 10))

    def delete_member():
        if member_id_entry.get().isdigit():
            success = sql.delete_member(int(member_id_entry.get()))
            if success:
                messagebox.showinfo("Success", "Member has been deleted successfully!")
            else:
                messagebox.showerror("Error", "Member not found.")
        else:
            messagebox.showerror("Error", "Invalid Member ID.")
        Member_window.destroy()
        Member_management(Toplevel())

    Button(tab2, text="Delete Member", bg="red", fg="white", command=delete_member).pack()

    Button(Member_window, text="Back", bg="red", fg="white", command=lambda: open_library_window(Member_window)).pack(pady=20)

# مدیریت کارکنان
def Staff_management(main_window):
    def open_edit_staff_window(staff):
        edit_window = Toplevel()
        edit_window.title("Edit Staff")
        edit_window.minsize(400, 300)
        Label(edit_window, text="Edit Staff", font=("", 18)).pack()
        name_entry = Entry(edit_window)
        name_entry.insert(0, staff[1])
        name_entry.pack()
        national_id_entry = Entry(edit_window)
        national_id_entry.insert(0, staff[2])
        national_id_entry.pack()
        phone_entry = Entry(edit_window)
        phone_entry.insert(0, staff[3])
        phone_entry.pack()
        address_entry = Entry(edit_window)
        address_entry.insert(0, staff[4])
        address_entry.pack()
        position_entry = Entry(edit_window)
        position_entry.insert(0, staff[5])
        position_entry.pack()
        Button(edit_window, text="Save", command=lambda: sql.update_staff(staff[0], name_entry.get(), national_id_entry.get(), phone_entry.get(), address_entry.get(), position_entry.get())).pack()
    main_window.withdraw()
    Staff_window = Toplevel()
    Staff_window.iconbitmap(icon_address)
    Staff_window.title("Library Management")
    Staff_window.minsize(1080, 720)
    
    tab_control = ttk.Notebook(Staff_window)
    
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)

    tab_control.add(tab1, text="Staff Management")
    tab_control.add(tab2, text="Show/Delete/Edit Staff")
    tab_control.pack(expand=1, fill="both")
    
    # --- Tab 1: Add Staff ---
    Label(tab1, text="Staff Management", font=("", 18)).pack(pady=10)
    Label(tab1, text="Staff Name:").pack()
    staff_name_entry = Entry(tab1)
    staff_name_entry.pack()
    Label(tab1, text="National ID:").pack()
    national_id_entry = Entry(tab1)
    national_id_entry.pack()
    Label(tab1, text="Phone Number:").pack()
    phone_number_entry = Entry(tab1)
    phone_number_entry.pack()
    Label(tab1, text="Address:").pack()
    address_entry = Entry(tab1)
    address_entry.pack()
    Label(tab1, text="Position:").pack()
    position_entry = Entry(tab1)
    position_entry.pack()

    def submit_staff():
        if staff_name_entry.get() and national_id_entry.get():
            sql.add_staff(staff_name_entry.get(), national_id_entry.get(), phone_number_entry.get(), address_entry.get(), position_entry.get())
            messagebox.showinfo("Success", "Staff has been added successfully!")
        else:
            messagebox.showerror("Error", "Please fill all required fields.")
        Staff_window.destroy()
        Staff_management(Toplevel())

    Button(tab1, text="Submit", bg="green", fg="white", command=submit_staff).pack(pady=10)

    # --- Tab 2: Show/Delete/Edit Staff ---
    Label(tab2, text="List of Staff", font=("", 18)).pack(pady=10)

    staff_list = sql.get_staff()
    for staff in staff_list:
        staff_info = f"ID: {staff[0]}, Name: {staff[1]}, National ID: {staff[2]}, Phone: {staff[3]}, Position: {staff[4]}"
        Label(tab2, text=staff_info).pack()

        # افزودن دکمه ویرایش به هر کارمند
        Button(tab2, text="Edit", command=lambda s=staff: open_edit_staff_window(s)).pack()

    Label(tab2, text="Enter Staff ID to Delete:").pack(pady=(10, 0))
    staff_id_entry = Entry(tab2)
    staff_id_entry.pack(pady=(0, 10))

    def delete_staff():
        if staff_id_entry.get().isdigit():
            success = sql.delete_staff(int(staff_id_entry.get()))
            if success:
                messagebox.showinfo("Success", "Staff has been deleted successfully!")
            else:
                messagebox.showerror("Error", "Staff not found.")
        else:
            messagebox.showerror("Error", "Invalid Staff ID.")
        Staff_window.destroy()
        Staff_management(Toplevel())

    Button(tab2, text="Delete Staff", bg="red", fg="white", command=delete_staff).pack()

    Button(Staff_window, text="Back", bg="red", fg="white", command=lambda: open_library_window(Staff_window)).pack(pady=20)

# مدیریت وام‌ها (قرض دادن و برگشت کتاب)
def Deposit_management(main_window):
    main_window.withdraw()
    Deposit_window = Toplevel()
    Deposit_window.title("Deposit Management")
    Deposit_window.minsize(1080, 720)
    Deposit_window.iconbitmap(icon_address)

    tab_control = ttk.Notebook(Deposit_window)
    
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)

    tab_control.add(tab1, text="Add Deposit")
    tab_control.add(tab2, text="View Deposits")
    tab_control.add(tab3, text="Return Book")
    tab_control.pack(expand=1, fill="both")

    # --- Tab 1: Add Deposit ---
    Label(tab1, text="Add New Deposit", font=("", 18)).pack(pady=10)
    
    Label(tab1, text="Member ID:").pack(pady=(10, 0))
    member_id_entry = Entry(tab1)
    member_id_entry.pack(pady=(0, 10))

    Label(tab1, text="Book ID:").pack(pady=(10, 0))
    book_id_entry = Entry(tab1)
    book_id_entry.pack(pady=(0, 10))

    Label(tab1, text="Loan Period (days):").pack(pady=(10, 0))
    loan_period_entry = Entry(tab1)
    loan_period_entry.pack(pady=(0, 10))

    Label(tab1, text="Date Received (YYYY-MM-DD):").pack(pady=(10, 0))
    date_received_entry = Entry(tab1)
    date_received_entry.pack(pady=(0, 10))

    Label(tab1, text="Return Date (YYYY-MM-DD):").pack(pady=(10, 0))
    return_date_entry = Entry(tab1)
    return_date_entry.pack(pady=(0, 10))

    # --- Tab 2: View Deposits ---
    Label(tab2, text="List of Active Deposits", font=("", 18)).pack(pady=10)
    
    deposits = sql.get_deposits()
    for deposit in deposits:
        deposit_info = f"Loan ID: {deposit[0]}, Book ID: {deposit[1]}, Member ID: {deposit[2]}, Loan Period: {deposit[3]}, Loan Date: {deposit[4]}, Return Date: {deposit[5]}"
        Label(tab2, text=deposit_info).pack()

    # --- Tab 3: Return Book ---
    Label(tab3, text="Return Book", font=("", 18)).pack(pady=10)

    Label(tab3, text="Book ID:").pack(pady=(10, 0))
    return_book_id_entry = Entry(tab3)
    return_book_id_entry.pack(pady=(0, 10))

    Label(tab3, text="Member ID:").pack(pady=(10, 0))
    return_member_id_entry = Entry(tab3)
    return_member_id_entry.pack(pady=(0, 10))

    Label(tab3, text="Daily Penalty (for late returns):").pack(pady=(10, 0))
    daily_penalty_entry = Entry(tab3)
    daily_penalty_entry.pack(pady=(0, 10))

    def submit_return():
        if return_book_id_entry.get().isdigit() and return_member_id_entry.get().isdigit() and daily_penalty_entry.get().isdigit():
            success = sql.return_book(int(return_book_id_entry.get()), int(return_member_id_entry.get()), float(daily_penalty_entry.get()))
            if success:
                messagebox.showinfo("Success", "Book returned successfully!")
            else:
                messagebox.showerror("Error", "Error returning book.")
        else:
            messagebox.showerror("Error", "Please enter valid data.")
        Deposit_window.destroy()
        Deposit_management(Toplevel())

    Button(tab3, text="Return Book", bg="green", fg="white", command=submit_return).pack(pady=20)

    Button(Deposit_window, text="Back", bg="red", fg="white", command=lambda: open_library_window(Deposit_window)).pack(pady=20)

    def submit_deposit():
        if (member_id_entry.get().isdigit() and book_id_entry.get().isdigit() and 
            loan_period_entry.get().isdigit() and validate_date(date_received_entry.get()) and validate_date(return_date_entry.get())):
            
            # فراخوانی تابع lend_book با ورودی‌های کاربر
            sql.lend_book(book_id_entry.get(), member_id_entry.get(), loan_period_entry.get(), 
                          date_received_entry.get(), return_date_entry.get())
            messagebox.showinfo("Success", "Loan has been added successfully!")
        else:
            messagebox.showerror("Error", "Please enter valid data.")
        Deposit_window.destroy()
        Deposit_management(Toplevel())

    Button(tab1, text="Submit", bg="green", fg="white", command=submit_deposit).pack(pady=20)

def validate_date(date_text):
    """اعتبارسنجی فرمت تاریخ به شکل YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()

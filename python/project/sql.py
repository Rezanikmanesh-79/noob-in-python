import mysql.connector
from mysql.connector import Error
import datetime  # اضافه کردن ماژول datetime

def connect_to_db():
    """اتصال به پایگاه داده."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0113",
            database="library"
        )
        return conn
    except Error as err:
        print(f"Error: {err}")
        return None

def execute_query(query, params=None):
    """اجرای یک دستور SQL با پارامترها."""
    conn = connect_to_db()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor
    except Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def fetch_query(query, params=None):
    """اجرای یک دستور SQL با پارامترها و دریافت نتایج."""
    conn = connect_to_db()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def add_book(title, author, translator, subject, publisher, price):
    """افزودن کتاب به جدول Books."""
    query = """
    INSERT INTO Books (title, author, translator, subject, publisher, price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (title, author, translator, subject, publisher, price))

def get_books():
    """دریافت لیست تمام کتاب‌ها."""
    query = "SELECT * FROM Books"
    return fetch_query(query)

def delete_book(book_id):
    """حذف یک کتاب از جدول Books."""
    query = "DELETE FROM Books WHERE book_id = %s"
    execute_query(query, (book_id,))
    return True

def add_member(name, national_id, phone_number, address):
    """افزودن عضو به جدول Members."""
    query = """
    INSERT INTO Members (name, national_id, phone_number, address)
    VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (name, national_id, phone_number, address))

def get_members():
    """دریافت لیست تمام اعضا."""
    query = "SELECT * FROM Members"
    return fetch_query(query)

def delete_member(member_id):
    """حذف یک عضو از جدول Members."""
    query = "DELETE FROM Members WHERE member_id = %s"
    execute_query(query, (member_id,))
    return True

def add_staff(name, national_id, phone_number, address, position):
    """افزودن کارمند به جدول Staff."""
    query = """
    INSERT INTO Staff (name, national_id, phone_number, address, position)
    VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(query, (name, national_id, phone_number, address, position))

def get_staff():
    """دریافت لیست تمام کارکنان."""
    query = "SELECT * FROM Staff"
    return fetch_query(query)

def delete_staff(staff_id):
    """حذف یک کارمند از جدول Staff."""
    query = "DELETE FROM Staff WHERE staff_id = %s"
    execute_query(query, (staff_id,))
    return True

def lend_book(book_id, member_id, loan_period, date_received, return_date):
    # بررسی اینکه ورودی‌ها عددی هستند
    if not (book_id.isdigit() and member_id.isdigit() and loan_period.isdigit()):
        print("Invalid input: Book ID, Member ID, and Loan Period must be numeric.")
        return

    # بررسی فرمت صحیح تاریخ‌ها
    if not (validate_date(date_received) and validate_date(return_date)):
        print("Invalid input: Date format must be YYYY-MM-DD.")
        return

    conn = connect_to_db()
    if conn is None:
        return
    try:
        cursor = conn.cursor()

        # تبدیل ورودی‌ها به عدد صحیح
        book_id = int(book_id)
        member_id = int(member_id)
        loan_period = int(loan_period)

        # بررسی وجود کتاب و عضو در پایگاه داده
        cursor.execute("SELECT * FROM Books WHERE book_id = %s", (book_id,))
        book_exists = cursor.fetchone()
        if not book_exists:
            print("Invalid input: Book not found.")
            return

        cursor.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
        member_exists = cursor.fetchone()
        if not member_exists:
            print("Invalid input: Member not found.")
            return

        # ثبت اطلاعات قرض در جدول Loans
        cursor.execute("INSERT INTO Loans (book_id, member_id, loan_period, date_received, return_date) VALUES (%s, %s, %s, %s, %s)",
                       (book_id, member_id, loan_period, date_received, return_date))
        conn.commit()
        print("Book loaned successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.close()

def validate_date(date_text):
    """اعتبارسنجی فرمت تاریخ به شکل YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False




def get_deposits():
    """دریافت لیست تمام وام‌های فعال (کتاب‌هایی که هنوز برنگشته‌اند)."""
    query = """
    SELECT loan_id, book_id, member_id, loan_period, date_received, return_date 
    FROM Loans 
    WHERE actual_return_date IS NULL
    """
    return fetch_query(query)



def return_book(book_id, member_id, daily_penalty):
    """بازگشت کتاب و محاسبه جریمه دیرکرد."""
    query = "SELECT return_date FROM Loans WHERE book_id = %s AND member_id = %s"
    results = fetch_query(query, (book_id, member_id))
    
    if results:
        return_date = results[0][0]
        actual_return_date = datetime.date.today()
        
        if actual_return_date > return_date:
            days_late = (actual_return_date - return_date).days
            total_penalty = days_late * daily_penalty
        else:
            total_penalty = 0

        update_query = """
        UPDATE Loans
        SET actual_return_date = %s, late_penalty = %s
        WHERE book_id = %s AND member_id = %s
        """
        execute_query(update_query, (actual_return_date, total_penalty, book_id, member_id))
    return True
def update_book(book_id, title, author, translator, subject, publisher, price):
    """به‌روزرسانی اطلاعات کتاب"""
    query = """
    UPDATE Books 
    SET title=%s, author=%s, translator=%s, subject=%s, publisher=%s, price=%s 
    WHERE book_id=%s
    """
    execute_query(query, (title, author, translator, subject, publisher, price, book_id))

def update_member(member_id, name, national_id, phone_number, address):
    """به‌روزرسانی اطلاعات عضو"""
    query = """
    UPDATE Members SET name=%s, national_id=%s, phone_number=%s, address=%s 
    WHERE member_id=%s
    """
    execute_query(query, (name, national_id, phone_number, address, member_id))

def update_staff(staff_id, name, national_id, phone_number, address, position):
    """به‌روزرسانی اطلاعات کارمند"""
    query = """
    UPDATE Staff SET name=%s, national_id=%s, phone_number=%s, address=%s, position=%s
    WHERE staff_id=%s
    """
    execute_query(query, (name, national_id, phone_number, address, position, staff_id))

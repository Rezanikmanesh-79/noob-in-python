import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",   
        password="0113",   
        database="library" 
    )
    return connection

def create_books_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        translator VARCHAR(255),
        subject VARCHAR(255),
        publisher VARCHAR(255),
        publish_date DATE,
        price DECIMAL(10, 2)
    );
    """)

    connection.commit()
    connection.close()

def create_members_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Members (
        member_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        national_id VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20),
        address TEXT,
        membership_date DATE
    );
    """)

    connection.commit()
    connection.close()

def create_staff_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Staff (
        staff_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        national_id VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20),
        address TEXT,
        position VARCHAR(100),
        hire_date DATE  
    );
    """)

    connection.commit()
    connection.close()

def create_loans_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Loans (
        loan_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT NOT NULL,
        member_id INT NOT NULL,
        loan_period INT NOT NULL,
        date_received DATE NOT NULL,
        return_date DATE NOT NULL,
        actual_return_date DATE,
        late_penalty DECIMAL(10, 2),
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (member_id) REFERENCES Members(member_id)
    );
    """)

    connection.commit()
    connection.close()

def create_all_tables():
    create_books_table()
    create_members_table()
    create_staff_table()
    create_loans_table()

if __name__ == "__main__":
    create_all_tables()

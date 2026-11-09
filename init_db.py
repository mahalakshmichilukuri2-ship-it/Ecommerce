
import sqlite3
import config


def create_tables():
    conn = sqlite3.connect(config.DATABASE_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    # 1. Admin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            email VARCHAR(150) UNIQUE,
            password VARCHAR(255),
            profile_image VARCHAR(255)
        )
    """)

    # 2. Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            email VARCHAR(150) UNIQUE,
            password VARCHAR(255),
            profile_image VARCHAR(255)
        )
    """)

    # 3. Products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(150),
            description TEXT,
            category VARCHAR(100),
            price DECIMAL(10,2),
            image VARCHAR(255),
            admin_id INTEGER NOT NULL,
            FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
        )
    """)

    # 4. Customer address table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_address (
            address_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            full_name VARCHAR(100) NOT NULL,
            phone VARCHAR(10) NOT NULL,
            delivery_address TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            email VARCHAR(100),
            door_no VARCHAR(50),
            city VARCHAR(100),
            pincode VARCHAR(10),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    # 5. Orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            razorpay_order_id VARCHAR(100),
            razorpay_payment_id VARCHAR(100),
            amount DECIMAL(10,2),
            payment_status VARCHAR(30),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    """)

    # 6. Order items table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            product_name VARCHAR(200),
            quantity INTEGER,
            price DECIMAL(10,2),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    # 7. Admin password resets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_resets (
            email VARCHAR(255) PRIMARY KEY,
            otp_hash VARCHAR(60) NOT NULL,
            expires_at DATETIME NOT NULL,
            attempts INTEGER DEFAULT 0
        )
    """)

    # 8. User password resets
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_password_resets (
            reset_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email VARCHAR(255) UNIQUE NOT NULL,
            otp_hash VARCHAR(255) NOT NULL,
            expires_at DATETIME NOT NULL,
            attempts INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

    print("SQLite database and all 8 tables created successfully!")


if __name__ == "__main__":
    create_tables()

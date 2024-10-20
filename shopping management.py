import os
import mysql.connector
import time
# Function to connect to MySQL database

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        username="root",   # Replace with your MySQL username
        password="03april2008",   # Replace with your MySQL password
        database="shopping"   # Replace with your database name
    )

# Clear screen function

def clear_screen():
    os.system('cls')

# Center-aligned print function

def center_print(text):
    print(text.center(60))

#Functions defined for Admin Page
#Function to add a new product

def admin_menu(cursor, connection):
    while True:
        clear_screen()
        center_print("--- Admin Menu ---")
        center_print("1. Add Product")
        center_print("2. Update Product")
        center_print("3. Delete Product")
        center_print("4. View Products")
        center_print("5. Manage Admins")
        center_print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_product(cursor, connection)
        elif choice == "2":
            update_product(cursor, connection)
        elif choice == "3":
            delete_product(cursor, connection)
        elif choice == "4":
            view_products(cursor)
        elif choice == "5":
            manage_admins(cursor,connection)
        elif choice == "6":
            break
        else:
            center_print("Invalid choice. Please try again.")
            input()



# Functions defined for Customer page



def customer_menu(cursor):
    while True:
        clear_screen()
        center_print("--- Customer Menu ---")
        center_print("1. View Products")
        center_print("2. Add to Cart")
        center_print("3. View Cart")
        center_print("4. Update Cart")
        center_print("5. Checkout")
        center_print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_products_customer(cursor)
        elif choice == "2":
            add_to_cart(cursor)
        elif choice == "3":
            view_cart(cursor)
        elif choice == "4":
            update_cart(cursor)
        elif choice == "5":
            checkout(cursor)
        elif choice =="6":
            break
        else:
            center_print("Invalid choice. Please try again.")


#Function for welcome page and login

def admin_login(cursor):

    clear_screen()
    center_print("=== Admin Login ===")

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("SELECT * FROM admin_users WHERE username = %s AND password = %s", (username, password))
    admin = cursor.fetchone()

    if admin:
        center_print("Login successful!")
        input("Press Enter to continue...")
        return True
    else:
        center_print("Invalid username or password.")
        input("Press Enter to continue...")
        return False

def manage_admins(cursor, db):
    while True:
        clear_screen()
        center_print("=== Manage Admins ===")
        center_print("1. Add Admin")
      
            change_admin_password(cursor, db)
        elif choice == '3':
            delete_admin(cursor, db)
        elif choice == '4':
            break
        else:
            center_print("Invalid choice. Please try again.")
            input()

def delete_admin(cursor, db):
    print()
    username = input("Enter the admin username to delete: ")


    input("Press enter to continue...")

def change_admin_password(cursor, db):
    print()
    username = input("Enter admin username: ")
    old_password = input("Enter current password: ")
    if admin:
        new_password = input("Enter new password: ")

        # Update the password in the database
        cursor.execute("UPDATE admin_users SET password = %s WHERE username = %s", (new_password, username))
        db.commit()
        center_print("Password changed successfully.")
        input("Press enter to continue...")
    else:
        center_print("Invalid username or current password.")
        input("Press enter to continue...")

def add_admin(cursor, db):
    print()
    username = input("Enter new admin username: ")
    cursor.execute("INSERT INTO admin_users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    center_print("Admin user '" + username + "' added successfully.")
    input("Press enter to continue...")

def welcome_page():
    clear_screen()
    center_print("=" * 55)

    center_print(" WELCOME TO THE SHOPPING MANAGEMENT SYSTEM ")
    center_print("-" * 55)  # Separator line
    
    center_print(" Class: COMPUTER SCIENCE XII PCM ")
    center_print("=" * 55)

    time.sleep(1)
    center_print("\n")
    center_print("Please select an option:")
    center_print("1. Admin Login")
    center_print("2. Customer Page")
    center_print("3. Exit")

    choice = input("\nEnter your choice: ")
    return choice

def main():
    # Connect to MySQL
    connection = connect_db()
    cursor = connection.cursor()

    while True:
        choice = welcome_page()  # Show welcome page

        if choice == "1":  # Admin Login
            if admin_login(cursor):
                admin_menu(cursor, connection)  # If login is successful, enter Admin Menu
        elif choice == "2":  # Customer Page
            customer_menu(cursor)  # Go to customer menu
        elif choice == "3":  # Exit
            center_print("Thank you for using the system!")
            time.sleep(5)
            break
        else:
            center_print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

    # Close the database connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

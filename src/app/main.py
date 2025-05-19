from database.connection import DatabaseConnection

def main():
    db = DatabaseConnection()
    db.create_tables()
    print("Tables created successfully.")

if __name__ == "__main__":
    main()
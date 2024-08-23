
import mysql.connector
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",  
            database="database_name"  
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)
        return None
def insert_record(connection, record):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"  
        cursor.execute(insert_query, record)
        connection.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as error:
        print("Error inserting record:", error)
    finally:
        if cursor:
            cursor.close()
def main():
    connection = connect_to_database()
    if connection:
        try:
            data = (
                input("Enter value for column1: "),
                input("Enter value for column2: "),
                input("Enter value for column3: ")
            )
            # Insert the record into the table
            insert_record(connection, data)
        finally:
            connection.close()
            print("MySQL connection closed")
if __name__ == "__main__":
    main()

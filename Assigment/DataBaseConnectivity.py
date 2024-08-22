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
def fetch_data_from_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table_name")  
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as error:
        print("Error fetching data from table:", error)
        return None
    finally:
        if cursor:
            cursor.close()
def display_data(rows):
    if rows:
        for row in rows:
            print(row)  
    else:
        print("No data retrieved from the table")
def main():
    connection = connect_to_database()
    if connection:
        data = fetch_data_from_table(connection)
        if data:
            display_data(data)
        connection.close()
        print("MySQL connection closed")
if __name__ == "__main__":
    main()

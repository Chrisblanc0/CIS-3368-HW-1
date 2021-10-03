import mysql.connector
from mysql.connector import Error 

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print("Connection established successfully.")
    except Error as e:
        print(f"The error '{e}' has occured")
    return connection


conn = create_connection("cis3368.c3wbowheifjy.us-east-2.rds.amazonaws.com", "admin", "Morena.1974", "cis3368fall21")
cursor = conn.cursor(dictionary=True)
sql = "SELECT * FROM shoppinglist"
cursor.execute(sql)
rows = cursor.fetchall()


def execute_query(connection, query): #sends connection and query and executes query to get something back
    cursor = connection.cursor()
    try:
        cursor.execute(query)#try to execute the query on cursor
        connection.commit()
        print("Query executed successful") #if it works it will print this
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query): #reads the query
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occured")


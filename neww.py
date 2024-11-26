import mysql.connector as connector
from mysql.connector import Error
try:
    connection = connector.connect(
        host="localhost",
        user="root",
        password="Badru@32822334",
        database="test1",
        port=3306
    )
    print("djudjjs")
    if connection:
        print("connected to database")
    
        cursor=connection.cursor()

        # vulnerable query
        username=input("username: ")
        password=input("password: ")
        cursor.execute("SELECT *FROM accessinfo WHERE username = %s AND password = %s", (username, password))

        # execute and fetch result
        result = cursor.fetchone()
        if result:
            print("Login successful")
        else:
            print("Login Failed")

    # Close tthe connection
        connection.close()
except Error as e:
    print('error:    ', e)

 
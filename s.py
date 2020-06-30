import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "asdf"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'datacamp'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'datacamp' database

cursor.execute("CREATE DATABASE datacamp")

## executing the statement using 'execute()' method
#cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
#databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
#print(databases)

## showing one by one database
#for database in databases:
#    print(database)
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "asdf",
    database = "datacamp"
)

cursor = db.cursor()

## defining the Query
query = "SELECT name, user_name FROM users"

## getting 'name', 'user_name' columns from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
data = cursor.fetchall()

## Showing the data
for pair in data:
    print(pair)
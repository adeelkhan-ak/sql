import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "asdf",
    database = "datacamp"
)

cursor = db.cursor()

## defining the Query
query = "SELECT user_name FROM users"

## getting 'user_name' column from the table
cursor.execute(query)

## fetching all usernames from the 'cursor' object
usernames = cursor.fetchall()

## Showing the data
for username in usernames:
    print(username)
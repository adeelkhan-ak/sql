import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "asdf",
    database = "datacamp"
)

cursor = db.cursor()

## adding 'id' column to the 'users' table
## 'FIRST' keyword in the statement will add a column in the starting of the table
cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

cursor.execute("DESC users")

print(cursor.fetchall())
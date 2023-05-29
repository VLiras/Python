import mysql.connector

# No subir a Github

my_db = mysql.connector.connect(
    host = 'localhost',
    port = 3300, 
    user = 'root',
    password = 'base_Sql0204'
)

cursor = my_db.cursor()
text = 'DATABASES'
dbs = cursor.execute(f'SHOW {text}')
# dbs = cursor.execute('SHOW DATABASES')
for i in cursor:
    print(i)
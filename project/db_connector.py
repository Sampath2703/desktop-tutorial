import mysql.connector

db_con_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    database="D12_oops",
    password="Nani@2703"
)
cur_obj = db_con_obj.cursor()
print("database connected")

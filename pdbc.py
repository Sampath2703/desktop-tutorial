
import mysql.connector 

print(mysql.connector)

dbc = mysql.connector.connect(

host="localhost",
user="root",
database="d12",
password="Nani@2703"
)

print("connected successfully")

tableCreationQuery = """
create table  employees4(
    id int primary key ,
    name varchar(50) not null,
    age int,
    email varchar(50) not null unique,
    salary decimal(10,2) not null 
)

"""
# print(dbc)
print("dbc connected successfully")

cursor__ = dbc.cursor()
print(cursor__,"cursor__")

cursor__.execute(tableCreationQuery)
# print("table created successfully")

while True:
    print("1. add employee")
    print("2. read employees")
    print("3. update employee")
    print("4. delete employee")
    print("5. exit")

    a=int(input("enter your choice here :-- "))
    if a == 1:
        i=int(input("enter id here :-- "))
        n =input("enter name here :-- ")
        a = int(input("enter age here :-- "))
        e =input("enter email here :-- ")
        s = float(input("enter salary here  :--  "))
        queryInsertingEmp="insert into employees4 (id,name,age,email,salary) values (%s,%s,%s,%s,%s)"
        data=(i,n,a,e,s) 
        cursor__.execute(queryInsertingEmp,data) 
        dbc.commit() 
        print("emp addedd successfully.....")


    elif a == 2:
        queryReading = "select * from employees4"
        cursor__.execute(queryReading)
        data = cursor__.fetchall()
        for i in data:
            print(i)

    elif o == 3:

        queryReadingEmp="select * from employees"
        cursor__.execute(queryReadingEmp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])

        id=int(input("enter emp id to update the details of emp :-- "))
        idTobeUpdated=int(input("enter id here to update:-- "))
        ag=int(input("enter age here :-- "))
        sal=float(input("enter slaary here :--   "))

        queryUpdateEmp ="update employees set salary=%s,age=%s,id=%s where id = %s"
        data=(sal,ag,idTobeUpdated,id)   
        cursor__.execute(queryUpdateEmp,data)
        dbC.commit()

        print("emp updated successfyully....")

    elif o == 4:
        queryReadingEmp="select * from employees"
        cursor__.execute(queryReadingEmp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])

        print("choose id to dlete emp")   
        id=int(input("enter id to dleete emp :--  "))
        queryDeleteEmp="delete from employees where id =%s"
        data=(id,)
        cursor__.execute(queryDeleteEmp,data)
        dbC.commit()


        print("emp deleted successfully....") 
    else:
        break
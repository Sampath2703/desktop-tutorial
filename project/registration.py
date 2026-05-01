
class Registration:
    def __init__(self, n, ac_n, Amt, pas, c_p):
        from db_connection import cur_obj

        queryCreatingTable = """
        create table if not exists users(
        customer_id int primary key auto_increment,
        name varchar(50) not null unique,
        account_number varchar(16) not null unique,
        balance decimal(10,2) not null,
        password varchar(16) not null
        )
        """
        cur_obj.execute(queryCreatingTable)
        print("Table Created")

        if pas == c_p:
            q = "insert into users(name,account_number,balance,password) values(%s,%s,%s,%s)"
            data=(n, ac_n, Amt, pas)
            cur_obj.execute(q,data)
            from db_connection import db_con_obj
            db_con_obj.commit()
            print("user registered successfully")

            if True:
                from login import Login
                ac_num_Login=input("enter yr account number :--  ")
                p_Login=input("enter login password here :-- ")
                Login(ac_num_Login,p_Login)
        else:
            print("password nad confirm password not matched")
            
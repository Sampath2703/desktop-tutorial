class Login:
    def __init__(self, an, cp):
        from db_connector import cur_obj
        fetchQuery = "select * from users"
        cur_obj.execute(fetchQuery)
        usersData = cur_obj.fetchall()

        for i in usersData:
            if i[2] == an and i[4] == cp:
                print(f"login successful {i[1]}")
            else:
                print("Invalid Password")
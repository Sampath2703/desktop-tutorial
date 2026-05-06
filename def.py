def add():
    print(10 + 20)

add()


def mul():
    print(20 * 40)

mul()


def sub():
    print(30 - 20)

sub()


def div():
    print(20 / 5)

div()

def dashboard():
    print("Dashboard accessed")



def registration():
    global stored_email, stored_password
    
    stored_email = input("Enter email: ")
    p = input("Enter password: ")
    c_p = input("Confirm password: ")

    if p == c_p:
        
        print("Registration successful")
    else:
        print("Passwords do not match")

registration()



def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    e = "s@gmail.com"
    p = "12345678"

    if email == e and password == p:
        print("Login successful")
        dashboard()
    else:
        print("Login failed")

login()

def dashboard():
    print("Dashboard accessed")
dashboard()
import dbcreds
import mariadb


def hackerLogin():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        alias = input("Please type your username: ")
        password = input("Please type your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=? ", [alias, password])
        hackers=cursor.fetchall()
        print("userloggedin")
        print(hackers)
        user_id = hackers[0][0]
    except mariadb.ProgrammingError:
        print("Do you even SQL bro?")
    except mariadb.OperationalError:
        print("there seems to be something wrong with the connection")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
        return user_id
def newExploit():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        content = input("enter your new exploit here: ")
        cursor.execute("INSERT INTO exploits(content,user_id) VALUES(?)", [content,user_id])
        conn.commit()
        if(cursor.rowcount == 1):
            print("congrats new exploit has been created")
        else:
            print("Too bad exploit has not been created")
    except mariadb.ProgrammingError:
        print("Do you even SQL bro?")
    except mariadb.OperationalError:
        print("there seems to be something wrong with the connection")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
def seeALLExploits():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits")
        allExploits = cursor.fetchall()
        print(allExploits)
    except mariadb.ProgrammingError:
        print("Do you even SQL bro?")
    except mariadb.OperationalError:
        print("there seems to be something wrong with the connection")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
def allOtherExploits(user_id):
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE user_id!=?", [user_id])
        allExploits = cursor.fetchall()
        print(allExploits)
    except mariadb.ProgrammingError:
        print("Do you even SQL bro?")
    except mariadb.OperationalError:
        print("there seems to be something wrong with the connection")
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.rollback()
            conn.close()
def exitApplication():
    exit()

print("Choose from the following options")
print("Option1: Login Hacker")
print("Option2: Sign up hacker")
print("---------------------------------------")
option = input("Choose your option: ")
option == "1","2"
if option == "1":
    user_id = hackerLogin()
    while True:
        print("Choose from the following options:")  
        print("Option1:Enter a new exploit")  
        print("Option2:See all of their exploits")
        print("Option3:See all other exploits by everyone except for your own")
        print("Option4: exit application")
        option = input("Choose your option: ")
        options = "1","2","3","4"
        if option == "1":
           newExploit()
        elif option == "2":
          seeALLExploits()
        elif option == "3":
           allOtherExploits(user_id)
        elif option == "4":
            exitApplication()
            
elif option == "2":
    def hackerSignUp():
        try:
            conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
            cursor = conn.cursor()
            alias = input("Please type your username: ")
            password = input("Please type your password: ")
            if(len(password) < 6):
                print("passwords too short")
            else:
                cursor.execute("INSERT INTO hackers(alias, password) VALUES(?,?)", [alias, password])
                conn.commit()
            if(cursor.rowcount == 1):
                print("congrats user has been created")
            else:
                print("shame user not created")

        except mariadb.ProgrammingError:
            print("Do you even SQL bro?")
        except mariadb.OperationalError:
            print("there seems to be something wrong with the connection")
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()




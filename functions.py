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


def hackerLogin():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        alias = input("Please type your username: ")
        password = input("Please type your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias=? AND password=? ", [alias, password])
        hackers=cursor.fetchall
        print("userloggedin")
        print(hacker)
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


def newExploit():
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        content = input("enter your new exploit here: ")
        cursor.execute("INSERT INTO exploits(content) VALUES(?)", [content])
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


def allOtherExploits():
     try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits WHERE alias")
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
    try:
        conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
        cursor = conn.cursor()
        alias = input("Please type your username: ")
        password = input("Please type your password: ")
        if(len(password) < 6):
            print("passwords too short")
        else:
            cursor.execute("INSERT INTO cli_social_media(alias, password) VALUES(?,?)", [alias, password])
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





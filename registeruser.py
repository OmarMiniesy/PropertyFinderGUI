import mysql.connector

def RegisterFunction(username, email, gender, birthdate, firstname, lastname):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    info = [(username, email, gender, birthdate, firstname, lastname)]

    query = "INSERT INTO user(username,email,gender,birthdate,firstname,lastname) VALUES (%s, %s, %s, %s, %s, %s)"

    cursor.executemany(query, info)

    mydb.commit()

    mydb.close()

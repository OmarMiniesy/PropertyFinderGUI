import mysql.connector

def AddReviewFunction(agentnum, username, review, rating):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    info = [(agentnum, username, review, rating)]

    query = "INSERT INTO review(agentnum,uname,review,rating) VALUES (%s, %s, %s, %s)"

    cursor.executemany(query, info)

    mydb.commit()

    mydb.close()

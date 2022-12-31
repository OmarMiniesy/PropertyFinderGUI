import mysql.connector

def viewReviewFunction(agentnum):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "SELECT uname, review FROM review WHERE agentnum = %s"

    cursor.execute(query,(agentnum,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

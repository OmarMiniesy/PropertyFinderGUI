import mysql.connector

def viewCompanyRatingFunction(name):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "select avg(rating) from review join agent on review.agentnum = agent.phonenumber where brokercompanyname = %s"

    cursor.execute(query,(name,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

import mysql.connector

def query8funct(city, type):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "SELECT area, count(referencenum), avg(price/size) FROM property WHERE city = %s AND type =%s and size > 0 GROUP BY 1 order by 2 DESC limit 10"

    cursor.execute(query,(city, type,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

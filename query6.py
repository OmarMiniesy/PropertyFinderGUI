import mysql.connector

def query6funct(name):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "select area, avg(price/size), type, count(type) from property where city = %s and size > 0 group by 1,3"

    cursor.execute(query,(name,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

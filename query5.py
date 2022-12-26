import mysql.connector

def query5funct(name):
    mydb = mysql.connector.connect(
        host = "db4free.net",
        user = "omarmins",
        password = "omar1234",
        database = "propfinder",
    )

    cursor = mydb.cursor()

    query = "select type, avg(price/size) ,count(type) from property where developmentname =%s and size > 0 group by 1"

    cursor.execute(query,(name,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist
import mysql.connector

def query10funct(phonenum):
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "select price, type, size, bedrooms, bathrooms, city, area, developmentname, developmentlocation from property where agentnumber=%s"

    cursor.execute(query,(phonenum,))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

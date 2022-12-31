import mysql.connector

def query9funct():
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    query = "select count(distinct A.phonenumber), C.name, C.numberoflistings, avg(P.price/P.size), count(P.referencenum)/count(distinct A.phonenumber)from company C join agent A on C.name = A.brokercompanyname join property P on P.agentnumber = A.phonenumber where size > 0 Group by 2, 3 Order by 3 desc, 4 desc limit 5"

    cursor.execute(query)

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()    

    return resultlist

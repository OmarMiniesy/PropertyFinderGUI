import mysql.connector

def query7funct(city, pricelessthan, pricegreaterthan, amenity1, amenity2, amenity3): 
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "",
    )

    cursor = mydb.cursor()

    #info = [(city, pricelessthan, pricegreaterthan, amenity1)]

    query = "SELECT listing_date, type, size, price, developmentname FROM property JOIN amenity ON property.referencenum = amenity.referencenumber WHERE city = %s AND price < %s AND price > %s AND amenity in (%s, %s, %s)"

    cursor.execute(query, (city, pricelessthan, pricegreaterthan, amenity1, amenity2, amenity3))

    results = cursor.fetchall()

    resultlist = []
    for result in results:
        resultlist.append(result)

    mydb.commit()
    mydb.close()

    return resultlist

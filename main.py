import sys
from PyQt5.QtWidgets import *

from registeruser import RegisterFunction
from addreview import AddReviewFunction
from viewagentreview import viewReviewFunction
from brokercompanyrating import viewCompanyRatingFunction
from query5 import query5funct
from query6 import query6funct
from query7 import query7funct
from query8 import query8funct
from query9 import query9funct
from query10 import query10funct

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 300
        self.top = 50
        self.width = 1300
        self.height = 1000
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tab = bigwidget(self)
        self.setCentralWidget(self.tab)
        self.show()

class bigwidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.bigboy = QTabWidget()        

        #######        REGISTER TAB     ########
        self.Register = QWidget()
        self.bigboy.addTab(self.Register,"Register")
        self.Register.layout = QVBoxLayout(self)

        # CREATE THE INPUT FIELDS
        self.username = QLineEdit("Username")
        self.Register.layout.addWidget(self.username)
        self.Register.setLayout(self.Register.layout)
        self.email = QLineEdit("email")
        self.Register.layout.addWidget(self.email)
        self.Register.setLayout(self.Register.layout)
        self.gender = QLineEdit("Gender (M)")
        self.Register.layout.addWidget(self.gender)
        self.Register.setLayout(self.Register.layout)
        self.birthdate = QLineEdit("birthdate (year-month-day)")
        self.Register.layout.addWidget(self.birthdate)
        self.Register.setLayout(self.Register.layout)
        self.firstname = QLineEdit("firstname")
        self.Register.layout.addWidget(self.firstname)
        self.Register.setLayout(self.Register.layout)
        self.lastname = QLineEdit("lastname")
        self.Register.layout.addWidget(self.lastname)
        self.Register.setLayout(self.Register.layout)

        # SUBMIT BUTTON
        self.RegisterButton = QPushButton("REGISTER")
        self.registermessage = QMessageBox()
        self.registermessage.setText("Submitted")

        def regOnClick():
            RegisterFunction(self.username.text(), self.email.text(), self.gender.text(), self.birthdate.text(), self.firstname.text(), self.lastname.text())
            self.Register.layout.addWidget(self.registermessage)
            self.registermessage.exec_()
            
        self.RegisterButton.clicked.connect(regOnClick)
        self.Register.layout.addWidget(self.RegisterButton)
        self.Register.setLayout(self.Register.layout)

        # QUERY
        self.label1 = QLabel("Register User")
        self.Register.layout.addWidget(self.label1)
        self.Register.setLayout(self.Register.layout)


        ###### ADD REVIEW TAB ######
        self.AddReviews = QWidget()
        self.bigboy.addTab(self.AddReviews,"AddReview")
        self.AddReviews.layout = QVBoxLayout(self)

        #CREATE THE INPUT FIELDS
        self.revagentnum = QLineEdit("Agent Number")
        self.AddReviews.layout.addWidget(self.revagentnum)
        self.AddReviews.setLayout(self.AddReviews.layout)
        self.revusername = QLineEdit("Username")
        self.AddReviews.layout.addWidget(self.revusername)
        self.AddReviews.setLayout(self.AddReviews.layout)
        self.review = QLineEdit("review")
        self.AddReviews.layout.addWidget(self.review)
        self.AddReviews.setLayout(self.AddReviews.layout)
        self.rating = QLineEdit("rating")
        self.AddReviews.layout.addWidget(self.rating)
        self.AddReviews.setLayout(self.AddReviews.layout)  

        # SUBMIT BUTTON
        self.reviewButton = QPushButton("SUBMIT")
        self.reviewmessage = QMessageBox()
        self.reviewmessage.setText("Submitted")

        def revOnClick():
            AddReviewFunction(self.revagentnum.text(), self.revusername.text(), self.review.text(), self.rating.text())
            self.AddReviews.layout.addWidget(self.reviewmessage)
            self.reviewmessage.exec_()
        
        self.reviewButton.clicked.connect(revOnClick)
        self.AddReviews.layout.addWidget(self.reviewButton)
        self.AddReviews.setLayout(self.AddReviews.layout)

        # QUERY
        self.label2 = QLabel("Rate and Review an Agent")
        self.AddReviews.layout.addWidget(self.label2)
        self.AddReviews.setLayout(self.AddReviews.layout)


        ##### VIEW REVIEWS TAB #####
        self.ViewReviews = QWidget()
        self.bigboy.addTab(self.ViewReviews,"ViewReview") 
        self.ViewReviews.layout = QVBoxLayout(self)

        ### CREATE THE INPUT FIELDS
        self.revagentnum1 = QLineEdit("Agent Number")
        self.ViewReviews.layout.addWidget(self.revagentnum1)
        self.ViewReviews.setLayout(self.ViewReviews.layout)

        ### SUBMIT BUTTON AND RESULTS
        self.viewReviewButton = QPushButton("SUBMIT")

        def viewRev():
            viewreviewresults = viewReviewFunction(self.revagentnum1.text())
            
            self.reviewTable = QTableWidget()
            self.reviewTable.setRowCount(len(list(viewreviewresults)) + 1)
            self.reviewTable.setColumnCount(2)

            self.reviewTable.setItem(0, 0, QTableWidgetItem("username"))
            self.reviewTable.setItem(0, 1, QTableWidgetItem("review"))

            for x in range(len(viewreviewresults)):
                row = viewreviewresults[x]
                for i in range(2):
                    col = row[i]
                    self.reviewTable.setItem(x + 1,i,QTableWidgetItem(col))
            
            self.ViewReviews.layout.addWidget(self.reviewTable)
            self.ViewReviews.setLayout(self.ViewReviews.layout)
        
        self.viewReviewButton.clicked.connect(viewRev)
        self.ViewReviews.layout.addWidget(self.viewReviewButton)
        self.ViewReviews.setLayout(self.ViewReviews.layout)           
        
        ### QUERY
        self.label3 = QLabel("Get all reviews of certain Agent using phone number")
        self.ViewReviews.layout.addWidget(self.label3)
        self.ViewReviews.setLayout(self.ViewReviews.layout) 


        ##### RATING OF A BROKER COMPANY #####
        self.Rating = QWidget()
        self.bigboy.addTab(self.Rating,"CompanyRating")
        self.Rating.layout = QVBoxLayout(self)

        ### CREATE INPUT FIELDS
        self.companyname = QLineEdit("Company Name")
        self.Rating.layout.addWidget(self.companyname)
        self.Rating.setLayout(self.Rating.layout)        

        ### SUBMIT BUTTON AND RESULTS
        self.viewCompRating = QPushButton("SUBMIT")

        def compRating():
            viewCompRatingResults = viewCompanyRatingFunction(self.companyname.text())

            self.companyRatingTable = QTableWidget()
            self.companyRatingTable.setRowCount(1)
            self.companyRatingTable.setColumnCount(1)
            x = viewCompRatingResults[0][0]
            int_to_float1 = "{:5.4f}".format(x)
            self.companyRatingTable.setItem(0, 0, QTableWidgetItem(int_to_float1))
            self.Rating.layout.addWidget(self.companyRatingTable)
            self.Rating.setLayout(self.Rating.layout)


        self.viewCompRating.clicked.connect(compRating)
        self.Rating.layout.addWidget(self.viewCompRating)
        self.Rating.setLayout(self.Rating.layout)

        ### QUERY
        self.label4 = QLabel("Get aggregated rating of a company by giving its name")
        self.Rating.layout.addWidget(self.label4)
        self.Rating.setLayout(self.Rating.layout) 

        ##### location_pricepersize_typenum #####
        self.location_pricepersize_typenum = QWidget()
        self.bigboy.addTab(self.location_pricepersize_typenum,"location_pricepersize_typenum")
        self.location_pricepersize_typenum.layout = QVBoxLayout(self)

        ### CREATE INPUT FIELDS
        self.devlocation = QLineEdit("Development Location")
        self.location_pricepersize_typenum.layout.addWidget(self.devlocation)
        self.location_pricepersize_typenum.setLayout(self.location_pricepersize_typenum.layout) 

        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery5 = QPushButton("SUBMIT")

        def vq5():
            viewquery5results = query5funct(self.devlocation.text())
            
            self.query5table = QTableWidget()
            self.query5table.setRowCount(len(list(viewquery5results)) + 1)
            self.query5table.setColumnCount(3)

            self.query5table.setItem(0, 0, QTableWidgetItem("Unit Type"))
            self.query5table.setItem(0, 1, QTableWidgetItem("Avg Price/Sqm"))
            self.query5table.setItem(0, 2, QTableWidgetItem("Num of Units"))

            for x in range(len(viewquery5results)):
                row = viewquery5results[x]
                for i in range(0, 3, 1):
                    if (i == 0):
                        col = row[i]
                        self.query5table.setItem(x+1, 0, QTableWidgetItem(col))
                    if (i == 1):
                        float_to_int_q5 = "{:6.4f}".format(row[i])
                        self.query5table.setItem(x+1, 1, QTableWidgetItem(float_to_int_q5))
                    if (i == 2):
                        float_to_int_q52 = "{:10.0f}".format(row[i])
                        self.query5table.setItem(x+1, 2, QTableWidgetItem(float_to_int_q52))

            
            self.location_pricepersize_typenum.layout.addWidget(self.query5table)
            self.location_pricepersize_typenum.setLayout(self.location_pricepersize_typenum.layout)
        
        self.viewQuery5.clicked.connect(vq5)
        self.location_pricepersize_typenum.layout.addWidget(self.viewQuery5)
        self.location_pricepersize_typenum.setLayout(self.location_pricepersize_typenum.layout)        

        ### QUERY
        self.label5 = QLabel("For a given development, show the average price / sqm and the number of listings for each unit type")
        self.location_pricepersize_typenum.layout.addWidget(self.label5)
        self.location_pricepersize_typenum.setLayout(self.location_pricepersize_typenum.layout) 


        ##### city_pricepersizepertype #####
        self.city_pricepersizepertype = QWidget()
        self.bigboy.addTab(self.city_pricepersizepertype,"city_pricepersizepertype")
        self.city_pricepersizepertype.layout = QVBoxLayout(self)

        ### INPUT FIELDS
        self.cityname = QLineEdit("City")
        self.city_pricepersizepertype.layout.addWidget(self.cityname)
        self.city_pricepersizepertype.setLayout(self.city_pricepersizepertype.layout)

        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery6 = QPushButton("SUBMIT")

        def vq6():
            viewquery6results = query6funct(self.cityname.text())
            
            self.query6table = QTableWidget()
            self.query6table.setRowCount(len(list(viewquery6results)) + 1)
            self.query6table.setColumnCount(4)

            self.query6table.setItem(0, 0, QTableWidgetItem("Area"))
            self.query6table.setItem(0, 1, QTableWidgetItem("Avg Price/Sqm"))
            self.query6table.setItem(0, 2, QTableWidgetItem("Unit Type"))
            self.query6table.setItem(0, 3, QTableWidgetItem("Amount"))

            for x in range(len(viewquery6results)):
                row = viewquery6results[x]
                for i in range(0, 4, 1):
                    if (i == 0):
                        col = row[i]
                        self.query6table.setItem(x+1, 0, QTableWidgetItem(col))
                    if (i == 1):
                        float_to_int_q16 = "{:6.5f}".format(row[i])
                        self.query6table.setItem(x+1, 1, QTableWidgetItem(float_to_int_q16))
                    if (i == 2):
                        col = row[i]
                        self.query6table.setItem(x+1, 2, QTableWidgetItem(col))
                    if (i == 3):
                        float_to_int_q62 = "{:6.0f}".format(row[i])
                        self.query6table.setItem(x+1, 3, QTableWidgetItem(float_to_int_q62))

            
            self.city_pricepersizepertype.layout.addWidget(self.query6table)
            self.city_pricepersizepertype.setLayout(self.city_pricepersizepertype.layout)
        
        self.viewQuery6.clicked.connect(vq6)
        self.city_pricepersizepertype.layout.addWidget(self.viewQuery6)
        self.city_pricepersizepertype.setLayout(self.city_pricepersizepertype.layout)                

        ### QUERY
        self.label6 = QLabel("Show the properties in a city, with the avg price/sqm for each type in every area in the city")
        self.city_pricepersizepertype.layout.addWidget(self.label6)
        self.city_pricepersizepertype.setLayout(self.city_pricepersizepertype.layout)



        ##### properties_price_city_amenity #####
        self.properties_price_city_amenity = QWidget()
        self.bigboy.addTab(self.properties_price_city_amenity,"properties_price_city_amenity")
        self.properties_price_city_amenity.layout = QVBoxLayout(self)


        ### INPUT FIELDS
        self.cityname1 = QLineEdit("City")
        self.properties_price_city_amenity.layout.addWidget(self.cityname1)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        self.lessthanprice = QLineEdit("price less than")
        self.properties_price_city_amenity.layout.addWidget(self.lessthanprice)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        self.greaterthanprice = QLineEdit("price greater than")
        self.properties_price_city_amenity.layout.addWidget(self.greaterthanprice)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        self.amenity1 = QLineEdit("amenity1")
        self.properties_price_city_amenity.layout.addWidget(self.amenity1)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        self.amenity2 = QLineEdit("amenity2")
        self.properties_price_city_amenity.layout.addWidget(self.amenity2)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        self.amenity3 = QLineEdit("amenity3")
        self.properties_price_city_amenity.layout.addWidget(self.amenity3)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)


        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery7 = QPushButton("SUBMIT")

        def vq7():
            viewquery7results = query7funct(self.cityname1.text(), self.lessthanprice.text(), self.greaterthanprice.text(), self.amenity1.text(), self.amenity2.text(), self.amenity3.text())
            
            self.query7table = QTableWidget()
            self.query7table.setRowCount(len(list(viewquery7results)) + 1)
            self.query7table.setColumnCount(5)

            self.query7table.setItem(0, 0, QTableWidgetItem("Listing Date"))
            self.query7table.setItem(0, 1, QTableWidgetItem("type"))
            self.query7table.setItem(0, 2, QTableWidgetItem("size"))
            self.query7table.setItem(0, 3, QTableWidgetItem("Price"))
            self.query7table.setItem(0, 4, QTableWidgetItem("Development name"))

            for x in range(len(viewquery7results)):
                row = viewquery7results[x]
                for i in range(0, 5, 1):
                    if (i == 0):
                        col = row[i]
                        self.query7table.setItem(x+1, 0, QTableWidgetItem(col))
                    if (i == 1):
                        col = row[i]
                        self.query7table.setItem(x+1, 1, QTableWidgetItem(col))
                    if (i == 2):
                        col = "{:6.0f}".format(row[i])
                        self.query7table.setItem(x+1, 2, QTableWidgetItem(col))
                    if (i == 3):
                        float_to_int_q62 = "{:7.0f}".format(row[i])
                        self.query7table.setItem(x+1, 3, QTableWidgetItem(float_to_int_q62))
                    if (i == 4):
                        col = row[i]
                        self.query7table.setItem(x+1, 4, QTableWidgetItem(col))

            
            self.properties_price_city_amenity.layout.addWidget(self.query7table)
            self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)
        
        self.viewQuery7.clicked.connect(vq7)
        self.properties_price_city_amenity.layout.addWidget(self.viewQuery7)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)        
        
        ### QUERY
        self.label7 = QLabel("Show all the properties in a certain city in a given price range, with a given set of amenities")
        self.properties_price_city_amenity.layout.addWidget(self.label7)
        self.properties_price_city_amenity.setLayout(self.properties_price_city_amenity.layout)

        
        ##### TOP AREA #####
        self.toparea = QWidget()
        self.bigboy.addTab(self.toparea,"toparea")
        self.toparea.layout = QVBoxLayout(self)

        ### INPUT FIELDS
        self.city8 = QLineEdit("City")
        self.toparea.layout.addWidget(self.city8)
        self.toparea.setLayout(self.toparea.layout)
        self.type8 = QLineEdit("Type")
        self.toparea.layout.addWidget(self.type8)
        self.toparea.setLayout(self.toparea.layout)

        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery8 = QPushButton("SUBMIT")

        def vq8():
            viewquery8results = query8funct(self.city8.text(), self.type8.text())
            
            self.query8table = QTableWidget()
            self.query8table.setRowCount(len(list(viewquery8results)) + 1)
            self.query8table.setColumnCount(3)

            self.query8table.setItem(0, 0, QTableWidgetItem("Area"))
            self.query8table.setItem(0, 1, QTableWidgetItem("Num Of Listings"))
            self.query8table.setItem(0, 2, QTableWidgetItem("Avg Price/sqm "))

            for x in range(len(viewquery8results)):
                row = viewquery8results[x]
                for i in range(0, 3, 1):
                    if (i == 0):
                        col = row[i]
                        self.query8table.setItem(x+1, 0, QTableWidgetItem(col))
                    if (i == 1):
                        col = "{:6.0f}".format(row[i])
                        self.query8table.setItem(x+1, 1, QTableWidgetItem(col))
                    if (i == 2):
                        col = "{:6.5f}".format(row[i])
                        self.query8table.setItem(x+1, 2, QTableWidgetItem(col))

            self.toparea.layout.addWidget(self.query8table)
            self.toparea.setLayout(self.toparea.layout)
        
        self.viewQuery8.clicked.connect(vq8)
        self.toparea.layout.addWidget(self.viewQuery8)
        self.toparea.setLayout(self.toparea.layout)        

        ###QUERY
        self.label8 = QLabel("Show the top 10 areas in a given city by amount of inventory and price / sqm of a given unit type ")
        self.toparea.layout.addWidget(self.label8)
        self.toparea.setLayout(self.toparea.layout)       


        ##### TOP BROKER COMPANIES #####
        self.topcompany = QWidget()         
        self.bigboy.addTab(self.topcompany,"topcompany")
        self.topcompany.layout = QVBoxLayout(self)

        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery9 = QPushButton("Get Top 5 Companies")

        def vq9():
            viewquery9results = query9funct()
            
            self.query9table = QTableWidget()
            self.query9table.setRowCount(len(list(viewquery9results)) + 1)
            self.query9table.setColumnCount(5)

            self.query9table.setItem(0, 0, QTableWidgetItem("company name"))
            self.query9table.setItem(0, 1, QTableWidgetItem("num of listings"))
            self.query9table.setItem(0, 2, QTableWidgetItem("avg price/sqm"))
            self.query9table.setItem(0, 3, QTableWidgetItem("num of agents"))
            self.query9table.setItem(0, 4, QTableWidgetItem("avg listings per agent"))

            for x in range(len(viewquery9results)):
                row = viewquery9results[x]
                for i in range(0, 5, 1):
                    if (i == 0):
                        col = "{:8.0f}".format(row[i])
                        self.query9table.setItem(x+1, 3, QTableWidgetItem(col))
                    if (i == 1):
                        col = row[i]
                        self.query9table.setItem(x+1, 0, QTableWidgetItem(col))
                    if (i == 2):
                        col = "{:8.0f}".format(row[i])
                        self.query9table.setItem(x+1, 1, QTableWidgetItem(col))
                    if (i == 3):
                        col = "{:8.5f}".format(row[i])
                        self.query9table.setItem(x+1, 2, QTableWidgetItem(col))
                    if (i == 4):
                        col = "{:8.3f}".format(row[i])
                        self.query9table.setItem(x+1, 4, QTableWidgetItem(col))
            
            self.topcompany.layout.addWidget(self.query9table)
            self.topcompany.setLayout(self.topcompany.layout)
        
        self.viewQuery9.clicked.connect(vq9)
        self.topcompany.layout.addWidget(self.viewQuery9)
        self.topcompany.setLayout(self.topcompany.layout)        

        ### QUERY
        self.label9 = QLabel("Show the top 5 brokerage companies by the amount of listings they have, along with their avg price/sqm, number of agents, and average listings per agent")
        self.topcompany.layout.addWidget(self.label9)
        self.topcompany.setLayout(self.topcompany.layout)        


        ##### PROPERTIES BY AGENT #####
        self.properties_agent = QWidget()
        self.bigboy.addTab(self.properties_agent,"properties_agent")
        self.properties_agent.layout = QVBoxLayout(self)

        ### INPUT FIELDS 
        self.phonenum10 = QLineEdit("phone num")
        self.properties_agent.layout.addWidget(self.phonenum10)
        self.properties_agent.setLayout(self.properties_agent.layout)

        ### SUBMIT BUTTON AND RESULTS
        self.viewQuery10 = QPushButton("SUBMIT")

        def vq10():
            viewquery10results = query10funct(self.phonenum10.text())
            
            self.query10table = QTableWidget()
            self.query10table.setRowCount(len(list(viewquery10results)) + 1)
            self.query10table.setColumnCount(9)

            self.query10table.setItem(0, 0, QTableWidgetItem("price"))
            self.query10table.setItem(0, 1, QTableWidgetItem("type"))
            self.query10table.setItem(0, 2, QTableWidgetItem("size"))
            self.query10table.setItem(0, 3, QTableWidgetItem("Bedrooms"))
            self.query10table.setItem(0, 4, QTableWidgetItem("Bathrooms"))
            self.query10table.setItem(0, 5, QTableWidgetItem("city"))
            self.query10table.setItem(0, 6, QTableWidgetItem("area"))
            self.query10table.setItem(0, 7, QTableWidgetItem("dev name"))
            self.query10table.setItem(0, 8, QTableWidgetItem("dev location"))

            for x in range(len(viewquery10results)):
                row = viewquery10results[x]
                for i in range(0, 9, 1):
                    if (i == 0 or i == 2):
                        col = "{:6.0f}".format(row[i])
                        self.query10table.setItem(x+1, i, QTableWidgetItem(col))
                    else:
                        col = row[i]
                        self.query10table.setItem(x+1, i, QTableWidgetItem(col))                        

            
            self.properties_agent.layout.addWidget(self.query10table)
            self.properties_agent.setLayout(self.properties_agent.layout)
        
        self.viewQuery10.clicked.connect(vq10)
        self.properties_agent.layout.addWidget(self.viewQuery10)
        self.properties_agent.setLayout(self.properties_agent.layout)

        ### QUERY
        self.label10 = QLabel("Show all the properties listed by a specific agent given the phone number")
        self.properties_agent.layout.addWidget(self.label10)
        self.properties_agent.setLayout(self.properties_agent.layout)


        self.layout.addWidget(self.bigboy)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
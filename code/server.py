import random
from models.Endpoints.employee.companyCustomerRepEndpoint import CustomerRep
from models.Endpoints.employee.companyStorekeeperEndpoint import StoreKeeper
from models.Endpoints.employee.companyProductionPlannerEndpoint import ProductionPlanner
from models.Endpoints.customerEndpoint import Customer
from models.Endpoints.publicEndpoint import Public
from models.Endpoints.transporterEndpoint import Transporter
from models.setup import setupInstance
from models.userHandler.authentication import authentication
from models.userHandler.classes import databaseUser, auth_user, AllUsers
from flask_mysqldb import MySQL

# set Random Seed
auth_user.setRandomizer()
# setup flask
setup             = setupInstance
app               = setup.init(__name__)
sql               = MySQL(app)

# configure flask
setup             .configureApp(app)

with app.app_context():
  databaseUser.FlushAuth(sql) # removes any leftover user if any
  databaseUser.DefineAllUsers() # Adds all users

# Route endpoints
authentication    .Route(app,sql) # Authentication

CustomerRep       .Route(app,sql) # Company 
ProductionPlanner .Route(app,sql)
StoreKeeper       .Route(app,sql)
  
Customer          .Route(app,sql) # Customer
Public            .Route(app,sql)
Transporter       .Route(app,sql)


# set listener
setup             .setListener(app, __name__)


with app.app_context(): # Removes users
  databaseUser.FlushAuth(sql)

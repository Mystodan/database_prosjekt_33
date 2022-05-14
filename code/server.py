from internal.Endpoints.employee.companyCustomerRepEndpoint import CustomerRep
from internal.Endpoints.employee.companyStorekeeperEndpoint import StoreKeeper
from internal.Endpoints.employee.companyProductionPlannerEndpoint import ProductionPlanner
from internal.Endpoints.customerEndpoint import Customer
from internal.Endpoints.publicEndpoint import Public
from internal.Endpoints.transporterEndpoint import Transporter
from internal.setup import setupInstance
from internal.userHandler.authentication import authentication
from internal.userHandler.classes import databaseUser, auth_user
from flask_mysqldb import MySQL

# set Random Seed
auth_user         .setRandomizer()
# setup flask
setup             = setupInstance
app               = setup.init(__name__)
sql               = MySQL(app)
# configure flask
setup             .configureApp(app)  
# checks connection to database and handles values
setup             .checkAndPreprocessConnection(app,sql)
 
            
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

# Removes users after session
with app.app_context(): 
  databaseUser    .FlushAuth(sql)

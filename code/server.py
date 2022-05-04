from models.Endpoints.companyProductionPlannerEndpoint import ProductionPlanner
from models.Endpoints.customerEndpoint import Customer
from models.Endpoints.publicEndpoint import Public
from models.Endpoints.transporterEndpoint import Transporter
from models.setup import setupInstance
from models.authentication.handler import authentication
from models.Endpoints.companyCustomerRepEndpoint import CustomerRep
from flask_mysqldb import MySQL


# setup flask
setup = setupInstance
app = setup.init(__name__)
sql = MySQL(app)
# configure flask
setup.configureApp(app)
# Route flask
# Company
authentication.Route(app, sql)
CustomerRep.Route(app,sql)
ProductionPlanner.Route(app,sql)
# Customer
Customer.Route(app,sql)
Public.Route(app,sql)
Transporter.Route(app,sql)

# set listener
setup.setListener(app, __name__)
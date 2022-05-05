from models.Endpoints.employee.companyCustomerRepEndpoint import CustomerRep
from models.Endpoints.employee.companyProductionPlannerEndpoint import ProductionPlanner
from models.Endpoints.employee.companyStorekeeperEndpoint import StoreKeeper
from models.Endpoints.customerEndpoint import Customer
from models.Endpoints.publicEndpoint import Public
from models.Endpoints.transporterEndpoint import Transporter
from constants.REST import constantEndpoints as ep

from flask import request
def contains (want, list):
  if want in list :
    return True
  return False

def HandleAuthentication(cur):
  
  hasPasw = False
  data = request.get_json()
  if contains(",",request.get_data(as_text=True)  ) :
    hasPasw=True
  token = data['auth_token']
  password = ""
        
  if hasPasw :
    password = data['password']
        
  sql = 'SELECT * FROM `authentication` WHERE `authentication`.`Auth_Token` = "'+token+'" AND `authentication`.`password` ="'+password+'"'
  return cur.execute(sql), password

"""  SETUP IF ONE ENDPOINT PERMISSION INVOKES MORE ENDPOINT !!!!!
def enpointHandler(endpoint):
  example one permission (repres) gives access to customers etc.
"""

def invokeEndpoint(endpoint):
  if endpoint == ep.ENDPOINT_EMPLOYEE.CUSTOMER_REPRESENTATIVE : 
    CustomerRep.endpoint = endpoint

  if endpoint ==  ep.ENDPOINT_EMPLOYEE.PRODUCTION_PLANNER : 
    ProductionPlanner.endpoint = endpoint

  if endpoint ==  ep.ENDPOINT_EMPLOYEE.STOREKEEPER : 
    StoreKeeper.endpoint = endpoint

  if endpoint ==  ep.ENDPOINT_CUSTOMER : 
    Customer.endpoint = endpoint

  if endpoint ==  ep.ENDPOINT_PUBLIC : 
    Public.endpoint = endpoint

  if endpoint ==  ep.ENDPOINT_TRANSPORTER : 
    Transporter.endpoint = endpoint
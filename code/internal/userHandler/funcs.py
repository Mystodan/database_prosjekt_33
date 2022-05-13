from internal.Endpoints.employee.companyCustomerRepEndpoint import CustomerRep
from internal.Endpoints.employee.companyProductionPlannerEndpoint import ProductionPlanner
from internal.Endpoints.employee.companyStorekeeperEndpoint import StoreKeeper
from internal.Endpoints.customerEndpoint import Customer
from internal.Endpoints.publicEndpoint import Public
from internal.Endpoints.transporterEndpoint import Transporter
from constants.REST import constantEndpoints as ep
from constants.rules import rules
from .classes import auth_user, user
from flask import request

def contains (want, list):
  """Checks if list contains want

  Args:
      want (any): a variable that is contained within list
      list (any list): a list which contains values

  Returns:
      bool: state if want is found in list
  """
  if want in list :
    return True
  return False



def HandleAuthentication(cur):
  """Handles the authentication for restricted endpoints
  Args:
      cur (MySql.connection.cursor()): Connection to database
  """
  hasPasw = False # state if body contains password
  data = request.get_json() # gets request body as json
  if contains(",",request.get_data(as_text=True)) : # checks if request has another case
    hasPasw=True 
  try: # checks if body is appropriate
    token = data['auth_token'] 
  except: # return inappropriate state of function
    return (-1)
  password = "" # sets default password
        
  if hasPasw :
    password = data['password'] # sets custom password
  _t,_p = token,password
  if rules.SET_HASH_USER: # Hashing
    userHash = auth_user.getHash(token, password)
    _t,_p = userHash, userHash
  sql = 'SELECT * FROM `authentication` WHERE `authentication`.`Auth_Token` = "'+_t+'" AND `authentication`.`password` ="'+_p+'"'
  return cur.execute(sql),token, password # returns appropriate values

"""  SETUP IF ONE ENDPOINT PERMISSION INVOKES MORE ENDPOINT !!!!!
def enpointHandler(endpoint):
  example one permission (repres) gives access to customers etc.
"""

def invokeEndpoint(endpoint):
  """Invokes an endpoint for usage after authentication has passed

  Args:
      endpoint (string): endpoint to invoke
  """
  if endpoint == ep.ENDPOINT_EMPLOYEE.CUSTOMER_REPRESENTATIVE : 
    CustomerRep.endpoint = endpoint #invokes endpoint(CustomerRep)

  if endpoint ==  ep.ENDPOINT_EMPLOYEE.PRODUCTION_PLANNER : 
    ProductionPlanner.endpoint = endpoint #invokes endpoint(ProductionPlanner)

  if endpoint ==  ep.ENDPOINT_EMPLOYEE.STOREKEEPER : 
    StoreKeeper.endpoint = endpoint #invokes endpoint(StoreKeeper)

  if endpoint ==  ep.ENDPOINT_CUSTOMER : 
    Customer.endpoint = endpoint #invokes endpoint(Customer)

  if endpoint ==  ep.ENDPOINT_PUBLIC : 
    Public.endpoint = endpoint #invokes endpoint(Public)

  if endpoint ==  ep.ENDPOINT_TRANSPORTER : 
    Transporter.endpoint = endpoint #invokes endpoint(Transporter)
    

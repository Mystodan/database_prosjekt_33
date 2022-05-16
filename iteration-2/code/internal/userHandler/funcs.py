from internal.Endpoints.employee.companyCustomerRepEndpoint import CustomerRep
from internal.Endpoints.employee.companyProductionPlannerEndpoint import ProductionPlanner
from internal.Endpoints.employee.companyStorekeeperEndpoint import StoreKeeper
from internal.Endpoints.customerEndpoint import Customer
from internal.Endpoints.publicEndpoint import Public
from internal.Endpoints.transporterEndpoint import Transporter
from internal.common import contains
from constants.rules import rules
from .classes import auth_user
from flask import request

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
    try:
      password = data['password'] # sets custom password
    except:
      return (-1)
  _t,_p = token,password
  if rules.SET_HASH_USER: # Hashing
    userHash = auth_user.getHash(token, password)
    _t,_p = userHash, userHash
  try:
    sql = ('SELECT * FROM `authentication` WHERE `authentication`.`Auth_Token` = "'+_t+'" AND `authentication`.`password` ="'+_p+'"')
  except:
    return (-2) # return inappropriate state of function
  return cur.execute(sql),token, password # returns appropriate values

"""  SETUP IF ONE ENDPOINT PERMISSION INVOKES MORE ENDPOINT !!!!!
def enpointHandler(endpoint):
  example one permission (repres) gives access to customers etc.
"""

def invokeEndpoints(endpoint):
  """Invokes an endpoint for usage after authentication has passed

  Args:
      endpoint (string): endpoint to invoke
  """
  CustomerRep.endpoint = endpoint #invokes endpoint(CustomerRep)
  ProductionPlanner.endpoint = endpoint #invokes endpoint(ProductionPlanner)
  StoreKeeper.endpoint = endpoint #invokes endpoint(StoreKeeper)
  Customer.endpoint = endpoint #invokes endpoint(Customer)
  Public.endpoint = endpoint #invokes endpoint(Public)
  Transporter.endpoint = endpoint #invokes endpoint(Transporter)
    

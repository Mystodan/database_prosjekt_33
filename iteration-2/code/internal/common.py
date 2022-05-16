from flask import Response, request
from constants.credentials import isLoggedIn
from constants.REST import constants, error , http, constantEndpoints as ep
from constants.rules import rules
EP = ep.ENDPOINT_EMPLOYEE


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


def hasLoggedIn(inn , want): # checks if inn is equal to want
  return  inn == want

# DEPRECATED
def isAppropriate(inn , want, corrResp):
  if not inn == want:
    return Response(error.Login_NotLoggedIn, status = http.StatusForbidden )
  else : return corrResp
  
def preLogin (endpoint):
  resp = http.StatusUnauthorized
  if isLoggedIn:
    resp = http.StatusForbidden 
  return Response((error.Login_NotLoggedIn+error.Endpoint+ endpoint), status = resp )

def InvalidMethod(functioningMethods):
  return handleErr(error.Login_InvalidMethod+functioningMethods, http.StatusMethodNotAllowed )

def setMethods() :
  return constants.HTTP_METHODS

def formatPath(endpoint, action) :
  return "/"+endpoint+"/" +action

def handleErr(response,error):
  return Response(response, status = error)

def PreprocessEndpoint(endpoint, func, method,  sql):
  data = request.get_data()
  if contains(b'{', data) and contains(b'}', data):
    if hasLoggedIn(endpoint.endpoint , endpoint.want) or (rules.SET_LOGIN is False):
      return handleInvalidMethod(func, method, sql)
    else:
      return preLogin(endpoint.want)
  
  
def handleInvalidMethod(func, method, sql) :
  if request.method == method:
    return func(sql)
  else:
    return InvalidMethod(method)
  

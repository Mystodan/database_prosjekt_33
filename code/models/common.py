from pickle import FALSE
from flask_mysqldb import MySQL
from flask import Response, request
from constants.REST import constants, error, http, constantEndpoints as ep
from constants.rules import rules
EP = ep.ENDPOINT_EMPLOYEE

def getSql ( inn):
  return MySQL(inn) 

def hasLoggedIn(inn , want):
  return  inn == want

# DEPRECATED
def isAppropriate(inn , want, corrResp):
  if not inn == want:
    return Response(error.Login_NotLoggedIn, status = http.StatusForbidden )
  else : return corrResp
  
def preLogin (endpoint):
  return Response((error.Login_NotLoggedIn+error.Endpoint+ endpoint), status = http.StatusForbidden )

def InvalidMethod(functioningMethods):
  return handleErr(error.Login_InvalidMethod+functioningMethods, http.StatusMethodNotAllowed )

def setMethods() :
  return constants.HTTP_METHODS

def formatPath(endpoint, action) :
  return "/"+endpoint+"/" +action

def handleErr(response,error):
  return Response(response, status = error)

def PreprocessEndpoint(endpoint, func, method,  sql):
  request.get_data()
  if hasLoggedIn(endpoint.endpoint , endpoint.want) or (rules.SET_LOGIN is False):
    return handleInvalidMethod(func, method, sql)
  else:
    return preLogin(endpoint.want)
  
def handleInvalidMethod(func, method, sql) :
  if request.method == method:
    return func(sql)
  else:
    return InvalidMethod(method)
  

from flask_mysqldb import MySQL
from flask import Response
from constants.REST import http, constantEndpoints as ep
EP = ep.ENDPOINT_EMPLOYEE

def getSql ( inn):
  return MySQL(inn) 

def isAppropriate(inn , want, corrResp):
  match inn == want:
    case False : return Response("Login first", status = http.StatusForbidden )
    case _ : return corrResp
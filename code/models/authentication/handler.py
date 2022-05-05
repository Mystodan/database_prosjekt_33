from flask import Response, request
from constants.REST import http, constants
from models.common import InvalidMethod
from .classes import user
from .funcs import HandleAuthentication, invokeEndpoint


class authentication():
  User = user
  def Route(app , sql):
    @app.route('/', methods = constants.HTTP_METHODS)
    def login() :
      if request.method != 'POST':
        return InvalidMethod('POST')

      cur = sql.connection.cursor()
      auth, password = HandleAuthentication(cur)
     
      if not auth:
        return Response("Bad Login", status = http.StatusNotAcceptable )
        
      auth = cur.fetchone()  
      token, password, endpoint = auth[0], auth[1], auth[2]
      if authentication.User.checkUser(token,password,endpoint) :
        return Response("Already signed in as "+endpoint, status = http.StatusOk)
      authentication.User.setUser(token,password,endpoint)
      
      invokeEndpoint(endpoint)

      return Response("Signed in as :"+endpoint, status = http.StatusOk)
        
      
      
        



  
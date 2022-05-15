from flask import Response, request
from constants.credentials import Credentials
from constants.REST import http, constants
from internal.common import InvalidMethod,contains
from .classes import user
from .funcs import HandleAuthentication, invokeEndpoints


class authentication():
  User = user
  
  def Route(app , sql):
    @app.route('/login', methods = constants.HTTP_METHODS)
    def auth_login() : return authentication.login(app,sql)
  
  def login(app,sql):
      if request.method != 'POST':
        return InvalidMethod('POST')
      data = request.get_data()
      if not (contains(b'{', data) and contains(b'}', data)):
        return authentication.Bad_request()
      cur = sql.connection.cursor()
      
      if HandleAuthentication(cur) == (-1) :
        return authentication.Bad_request()
      if HandleAuthentication(cur) == (-2) :
        return authentication.Bad_login()
      
      
      auth, token, password  = HandleAuthentication(cur)
    
        
      auth = cur.fetchone()  
      endpoint = auth[2]
      if authentication.User.checkUser(token,password,endpoint) :
        return Response("Already signed in as "+endpoint, status = http.StatusAlreadyReported)
      authentication.User.setUser(token,password,endpoint)
      Credentials.login = True
      
      invokeEndpoints(endpoint)

      return Response("Signed in as :"+endpoint, status = http.StatusOk)
    
  def Bad_login ():
    return Response("Invalid Token or Password", status = http.StatusNotAcceptable )
        
  def Bad_request ():
    return Response("Invalid request body", status = http.StatusBadRequest )
        
      
      
        



  
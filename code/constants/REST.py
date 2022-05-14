
class constants(object):
  HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
  
class constantEndpoints(object):
  
  ENDPOINT_CUSTOMER     = "customer"
  ENDPOINT_TRANSPORTER  = "transporter"
  ENDPOINT_PUBLIC       = "public"

  class ENDPOINT_EMPLOYEE(object):  
    ENDPOINT    = "employee"
    CUSTOMER_REPRESENTATIVE = "customer_rep"
    STOREKEEPER = "storekeeper"
    PRODUCTION_PLANNER = "production_planner"
                  
  
class http(object):
# The server encountered an unexpected condition that prevented it from fulfilling the request.
  StatusInternalServerError = 500
# The request could not be understood by the server due to incorrect syntax. 
# The client SHOULD NOT repeat the request without modifications.
  StatusBadRequest = 400
# Indicates that the request requires user authentication information. 
# The client MAY repeat the request with a suitable Authorization header field
  StatusUnauthorized = 401
# Unauthorized request. The client does not have access rights to the content. 
# Unlike 401, the client’s identity is known to the server.
  StatusForbidden = 403
# The request HTTP method is known by the server but has been disabled and cannot be used for that resource.
  StatusMethodNotAllowed = 405
# The server doesn’t find any content.
# That conforms, to the criteria given by the user agent in the Accept header sent in the request.
  StatusNotAcceptable = 406
# Allows a client to tell the server that the same resource (with the same binding) was mentioned earlier. 
# It never appears as a true HTTP response code in the status line, and only appears in bodies.
  StatusAlreadyReported = 208
# Indicates that the request has succeeded and a new resource has been created as a result.
  StatusCreated = 201
# Indicates that the request has succeeded.
  StatusOk = 200
  
  
class error(object):
  Login_InvalidMethod = "LOGIN: Invalid method, Use "
  
  Endpoint = ": "

  Login_NotLoggedIn = ("LOGIN: Login as correct user first")
  
  Body_Invalid = "BODY: Invalid input"
  
  Query_Duplicate = "QUERY: Input already exists within database"
  
  No_DataBase_Found = "FATAL ERROR: Database connection not found"
  DataBase_Found = " * SERVER: Database connection found!"

from flask import Response, request, jsonify
from constants.REST import http, constants
from models.Endpoints.companyProductionPlannerEndpoint import ProductionPlanner
from models.Endpoints.companyStorekeeperEndpoint import StoreKeeper
from models.Endpoints.customerEndpoint import Customer
from models.Endpoints.publicEndpoint import Public
from models.Endpoints.transporterEndpoint import Transporter
from .classes import user
from .funcs import HandleAuthentication
from models.Endpoints.companyCustomerRepEndpoint import CustomerRep
from constants.REST import http,constantEndpoints as ep


class authentication():
  User = user
  def Route(app , sql):
    @app.route('/', methods = constants.HTTP_METHODS)
    def handler() :
      
      cur = sql.connection.cursor()
      if request.method != 'POST':
        return Response("LOGIN: Invalid method, Use Post", status = http.StatusMethodNotAllowed )
      else :
        auth, password = HandleAuthentication(cur)
        if not auth:
         return Response("Bad Login", status = http.StatusNotAcceptable )
          
        auth = cur.fetchone()  
        token, password, endpoint = auth[0], auth[1], auth[2]
        if authentication.User.checkUser(token,password,endpoint) :
          return Response("Already signed in as "+endpoint, status = http.StatusOk)
        authentication.User.setUser(token,password,endpoint)
      
      match endpoint:
        case ep.ENDPOINT_EMPLOYEE.CUSTOMER_REPRESENTATIVE : 
          CustomerRep.endpoint = endpoint
   
        case ep.ENDPOINT_EMPLOYEE.PRODUCTION_PLANNER : 
          ProductionPlanner.endpoint = endpoint
   
        case ep.ENDPOINT_EMPLOYEE.STOREKEEPER : 
          StoreKeeper.endpoint = endpoint

        case ep.ENDPOINT_CUSTOMER : 
          Customer.endpoint = endpoint
    
        case ep.ENDPOINT_PUBLIC : 
          Public.endpoint = endpoint

        case ep.ENDPOINT_TRANSPORTER : 
          Transporter.endpoint = endpoint

      return Response("Signed in as :"+endpoint, status = http.StatusOk)
        
      
      
        



  
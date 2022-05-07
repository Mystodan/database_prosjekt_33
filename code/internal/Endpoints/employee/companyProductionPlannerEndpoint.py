from email.policy import default
from flask import (
  request,
  jsonify
)
from constants.REST import (
  error,
  http, 
  constantEndpoints as ep
  )
from internal.common import (
  setMethods, 
  formatPath, 
  handleErr,
  PreprocessEndpoint,
  )

class ProductionPlanner ():
  want = ep.ENDPOINT_EMPLOYEE.PRODUCTION_PLANNER
  endpoint = ""
  def setPath (action) :
    return  formatPath(ep.ENDPOINT_EMPLOYEE.ENDPOINT, action) 
  
  def Route(app,sql):
    setPath = ProductionPlanner.setPath
    
    # Fills an production plan and adds it to the database
    @app.route(setPath('/fill_plan'),methods=setMethods())
    def prod_plan_fill_plan(): return PreprocessEndpoint(ProductionPlanner, ProductionPlanner.fill_plan, 'POST',sql )
    
    
  def fill_plan(mysql) : 
     
    data = request.get_json()
    try:
      employeeNumber=data['employeeNumber']
      startDate=data['startDate']
      endDate=data['endDate']
      typeID=data['typeID']
      quantity=data['quantity']
    except:
       return handleErr(error.Body_Invalid, http.StatusBadRequest)
    
    cur=mysql.connection.cursor()
    try:
      add_plan = cur.execute("INSERT INTO `productionplan` (`employeeNumber`, `typeID`, `startDate`, `endDate`, `quantity`) VALUES (%s, %s, %s, %s, %s)", ((employeeNumber,), (typeID,), (startDate,), (endDate,), (quantity,)))
      mysql.connection.commit()

      change_info = cur.execute("SELECT * FROM `productionplan`")
    except:
      return handleErr(error.Query_Duplicate+ error.Endpoint + startDate, http.StatusBadRequest)
    if change_info > 0:
        change_info = cur.fetchall()
    cur.close()
    return jsonify(change_info),http.StatusCreated
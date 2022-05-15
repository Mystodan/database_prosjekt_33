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

class StoreKeeper ():
  """class handler for Store Keeper Endpoint
  """
  want = ep.ENDPOINT_EMPLOYEE.STOREKEEPER
  endpoint = ""
  def setPath (action) :
    return  formatPath(ep.ENDPOINT_EMPLOYEE.ENDPOINT, action) 
  
  def Route(app,mysql):
    """Routes Store Keeper Endpoint

    Args:
        app (Flask): Application to route enpoints to
        mysql (_type_): Database to get data from

    Returns:
        _type_: body and status code
    """
    setPath = StoreKeeper.setPath
    
    # Retrieve all skis that have the state "available"
    @app.route(setPath('/get_available'),methods=setMethods())
    def company_store_get_available(): return PreprocessEndpoint(StoreKeeper,StoreKeeper.get_available,'GET', mysql)
        
    # Change the info of a newly made ski type
    @app.route(setPath('/change_info'),methods=setMethods())
    def company_store_change_info(): return PreprocessEndpoint(StoreKeeper,StoreKeeper.change_info, 'PUT', mysql)
        
    # Changes the state of an order to from "available" to "ready"
    @app.route(setPath('/change_state_ready'),methods=setMethods())
    def company_store_cancel_order(): return PreprocessEndpoint(StoreKeeper,StoreKeeper.change_state_ready,'PUT', mysql)
        
    # Creates a new record for newly produced skis
    @app.route(setPath('/create_record'),methods=setMethods())
    def company_store_create_record(): return PreprocessEndpoint(StoreKeeper,StoreKeeper.create_record, 'POST',mysql)
          
    
  def get_available(mysql) :
    cur=mysql.connection.cursor()

    orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'available'")

    if orders >0:
        orders = cur.fetchall()
    cur.close()
    return jsonify(orders), http.StatusCreated
      
  def change_info(mysql):
    data = request.get_json()
    try:
      typeID=data['typeID']
      info=data['info']
    except :
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    
    cur=mysql.connection.cursor()

    change_state = cur.execute("UPDATE `skitype` SET `description`=%s WHERE `typeID`=%s", [(info,), (typeID,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `skitype`")

    if change_info > 0:
        change_info = cur.fetchall()
    
    cur.close()
    return jsonify(change_info),http.StatusCreated

  def change_state_ready(mysql):
    data = request.get_json()
    
    try:
      orderNumber=data['orderNumber']
    except :
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    cur=mysql.connection.cursor()

    change_state = cur.execute("UPDATE `orders` SET `state`='ready' WHERE `orderNumber`=%s AND `state`='available'", [(orderNumber,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `orders`")

    if change_info > 0:
        change_info = cur.fetchall()
  
    cur.close()
    return jsonify(change_info),http.StatusCreated

  def create_record(mysql):
    data = request.get_json()
    
    try:
      typeID=data['typeID']
      length=data['length']
      reserved=data['reserved']
    except:
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    
    cur=mysql.connection.cursor()

    add_order = cur.execute("INSERT INTO `ski` (`typeID`, `length`, `reserved`) VALUES (%s, %s, %s)", [(typeID,),(length,),(reserved,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `ski`")

    if change_info > 0:
        change_info = cur.fetchall()
    cur.close()
    return jsonify(change_info),http.StatusCreated
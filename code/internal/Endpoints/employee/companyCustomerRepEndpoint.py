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

class CustomerRep ():
  want = [ep.ENDPOINT_EMPLOYEE.CUSTOMER_REPRESENTATIVE]
  endpoint = ""
  def setPath (action) :
    return  formatPath(ep.ENDPOINT_EMPLOYEE.ENDPOINT, action) 

  def Route(app,sql):
    setPath = CustomerRep.setPath

    # Retrieve all orders that have the specified value as their "state"
    @app.route(setPath('/get_state'), methods=setMethods())
    def customer_rep_get_state():return PreprocessEndpoint( CustomerRep,CustomerRep.get_state, 'GET',  sql)
      
    # Change the state of an order from "new" to "open"
    @app.route(setPath('/change_state_open'),methods=setMethods())
    def customer_rep_change_state_open(): return PreprocessEndpoint(CustomerRep,CustomerRep.change_state_open, 'PUT',   sql)

    # Change the state of an order from "open" to "available"
    @app.route(setPath('/change_state_available'),methods=setMethods())
    def customer_rep_change_state_available(): return PreprocessEndpoint(CustomerRep,CustomerRep.change_state_available, 'PUT',  sql)
        
    # Fills an order and creates a shipment request for a shipment
    @app.route(setPath('/fill_order'),methods=setMethods())
    def customer_rep_fill_order(): return PreprocessEndpoint(CustomerRep, CustomerRep.fill_order, 'POST',   sql)
    
  
  def get_state(mysql):
    data = request.get_json()
    try:
      state= data['state']
    except :
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    cur=mysql.sql.connection.cursor()
    orders = cur.execute("SELECT * FROM `orders` WHERE `state`=%s",[(state,)])
    if orders > 0:
        orders = cur.fetchall()
    cur.close()
    return jsonify(orders), http.StatusOK

      
  def change_state_open(mysql):
    data = request.get_json()
    try:
      orderNumber=data['orderNumber']
    except:
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    cur=mysql.connection.cursor()
    change_state = cur.execute("UPDATE `orders` SET `state`='open' WHERE `orderNumber`=%s AND `state`='new'", [(orderNumber,)])
    mysql.connection.commit()
    change_info = cur.execute("SELECT * FROM `orders`")
    if change_info > 0:
        change_info = cur.fetchall()
    cur.close()
    return jsonify(change_info),http.StatusOK
  
      
  def change_state_available(mysql):
    data = request.get_json()
    try:
      orderNumber=data['orderNumber']
    except: 
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    
    cur=mysql.connection.cursor()
    change_state = cur.execute("UPDATE `orders` SET `state`='available' WHERE `orderNumber`=%s AND `state`='open'",[(orderNumber,)])
    mysql.connection.commit()
    change_info = cur.execute("SELECT * FROM `orders`")
    if change_info > 0:
        change_info = cur.fetchall()
    cur.close()
    return jsonify(change_info),http.StatusOk
  
  def fill_order(mysql):
    data = request.get_json()
    try:
      transporterID=data['transporterID']
      orderNumber=data['orderNumber']
      shippingAddress=data['shippingAddress']
      pickUpDate=data['pickUpDate']
    except: 
      return handleErr(error.Body_Invalid, http.StatusBadRequest)
    
    cur=mysql.connection.cursor()

    change_state = cur.execute("UPDATE `orders` SET `state`='shipped' WHERE `orderNumber`=%s AND `state`='ready'", [(orderNumber,)])

    add_shipment = cur.execute("INSERT INTO `shipment` (`transporterID`, `orderNumber`, `shippingAddress`, `pickUpDate`, `state`) VALUES (%s, %s, %s, %s, 'ready')", ([(transporterID,)], [(orderNumber,)], [(shippingAddress,)], [(pickUpDate,)]))
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `orders`")

    if change_info > 0:
        change_info = cur.fetchall()
    cur.close()
    return jsonify(change_info),http.StatusCreated
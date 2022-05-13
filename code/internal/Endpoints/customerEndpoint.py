from flask import (
  request, 
  jsonify
  )
from internal.common import setMethods
from internal.common import PreprocessEndpoint
from constants.REST import (
    http,
    constantEndpoints as ep
  )


class Customer ():
  """class handler for Customer Endpoint
  """
  want = ep.ENDPOINT_CUSTOMER
  endpoint = ""
  def Route(app,mysql):
    """Routes Customer Endpoint

    Args:
        app (Flask): Application to route enpoints to
        mysql (_type_): Database to get data from

    Returns:
        _type_: body and status code
    """
    # Retrieve a list of orders that a customer has made (with an optional since filter)
    @app.route('/get_orders',methods=['GET'])
    def customer_get_orders(): return PreprocessEndpoint(Customer, Customer.get_orders,'GET', mysql)

    # Retrieve all information about an order and its state
    @app.route('/get_order_info',methods=['GET'])
    def customer_get_order_info(): return PreprocessEndpoint(Customer, Customer.get_order_info,'GET', mysql)


    # Places a new order with a specified quantity
    @app.route('/place_order',methods=['POST'])
    def customer_place_order(): return PreprocessEndpoint(Customer, Customer.place_order,'POST', mysql)


    # Changes the state of an order to "cancelled"
    @app.route('/cancel_order',methods=['PUT'])
    def customer_cancel_order(): return PreprocessEndpoint(Customer, Customer.cancel_order, 'PUT', mysql)

    # Retrieve a summary of ongoing production plans within a specified period
    @app.route('/get_plan_summary',methods=setMethods())
    def customer_get_plan_summary(): return PreprocessEndpoint(Customer, Customer.get_plan_summary,'GET', mysql)

    # Deletes an order with a specified "orderNumber"
    @app.route('/delete_order',methods=setMethods())
    def customer_delete_order(): return PreprocessEndpoint(Customer, Customer.delete_order,'DELETE', mysql)
  
  
  
# Function which retrieves a list of orders that a customer has made (with an optional since filter)
  def get_orders(mysql):
    data = request.get_json()
    customerID=data['customerID']
    cur=mysql.connection.cursor()
    order = "SELECT customer.customerName, orders.* FROM `orders`, `customer` WHERE orders.customerID =%s AND orders.customerID = customer.customerID "
    exec = [(customerID,)]
    
    if len(data) == 2 :
      since=data['since']
      order = order + " AND  %s <= orders.date "
      exec = [(customerID,),(since,)]

    orders = cur.execute(order, exec)
    
    if orders >0:
        orders = cur.fetchall()
    cur.close()
    return (jsonify(orders),http.StatusCreated)
  
# Function which retrieves all information about an order and its state   
  def get_order_info(mysql):
    data = request.get_json()
    orderNumber=data['orderNumber']
    
    cur=mysql.connection.cursor()

    orders = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", [(orderNumber,)])

    if orders >0:
        orders = cur.fetchall()

    
    cur.close()
    return (jsonify(orders),http.StatusCreated)

# Function which places a new order with a specified quantity
  def place_order(mysql):
    data = request.get_json()
    quantity=data['quantity']
    customerID=data['customerID']
    
    cur=mysql.connection.cursor()

    add_order = cur.execute("INSERT INTO `orders` (`quantity`, `state`, `customerID`) VALUES (%s, 'new', %s)", [(quantity,), (customerID,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `orders`")

    if change_info > 0:
        change_info = cur.fetchall()

    cur.close()
    return jsonify(change_info),http.StatusCreated
 
# Function which changes the state of an order to "cancelled"   
  def cancel_order(mysql):
    data = request.get_json()
    orderNumber=data['orderNumber']
    
    cur=mysql.connection.cursor()

    change_state = cur.execute("UPDATE `orders` SET `state`='cancelled' WHERE `orderNumber`=%s", [(orderNumber,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `orders`")

    if change_info > 0:
        change_info = cur.fetchall()

    cur.close()
    return (jsonify(change_info),http.StatusCreated)

# Function which retrieves a summary of ongoing production plans within a specified period  
  def get_plan_summary(mysql):      
    data = request.get_json()
    startDate=data['startDate']
    endDate=data['endDate']
    
    cur=mysql.connection.cursor()

    orders = cur.execute("SELECT `typeID`, `quantity`, `startDate`, `endDate` FROM `productionplan` WHERE %s <= `startDate` AND %s >= `endDate`", [(startDate,), (endDate,)])

    if orders >0:
        orders = cur.fetchall()

    cur.close()
    return (jsonify(orders),http.StatusCreated)

# Function which deletes an order with a specified "orderNumber"    
  def delete_order(mysql):      
    data = request.get_json()
    orderNumber=data['orderNumber']
    
    cur=mysql.connection.cursor()

    delete_order = cur.execute("DELETE FROM `orders` WHERE `orderNumber`=%s", [(orderNumber,)])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `orders`")

    if change_info > 0:
        change_info = cur.fetchall()

    cur.close()
    return (jsonify(change_info),http.StatusCreated)


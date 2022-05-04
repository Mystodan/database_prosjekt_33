from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class Customer ():
  want = ep.ENDPOINT_CUSTOMER
  endpoint = ""
  def Route(app,mysql):
    # Retrieve a list of orders that a customer has made (with an optional since filter)
    @app.route('/get_orders',methods=['GET'])
    def get_orders():
        
        if request.method == 'GET':
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
            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal



    # Retrieve all information about an order and its state
    @app.route('/get_order_info',methods=['GET'])
    def get_order_info():
        
        if request.method == 'GET':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            orders = cur.execute("SELECT * FROM `orders` WHERE `orderNumber`=%s", [(orderNumber,)])

            if orders >0:
                orders = cur.fetchall()

            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal

    # Places a new order with a specified quantity
    @app.route('/place_order',methods=['POST'])
    def place_order():
        
        if request.method == 'POST':
            data = request.get_json()
            quantity=data['quantity']
            customerID=data['customerID']
            
            cur=mysql.connection.cursor()

            add_order = cur.execute("INSERT INTO `orders` (`quantity`, `state`, `customerID`) VALUES (%s, 'new', %s)", [(quantity,), (customerID,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()

            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Changes the state of an order to "cancelled"
    @app.route('/cancel_order',methods=['PUT'])
    def cancel_order():
        
        if request.method == 'PUT':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `orders` SET `state`='cancelled' WHERE `orderNumber`=%s", [(orderNumber,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()

            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Retrieve a summary of ongoing production plans within a specified period
    @app.route('/get_plan_summary',methods=['GET'])
    def get_plan_summary():
        
        if request.method == 'GET':
            data = request.get_json()
            startDate=data['startDate']
            endDate=data['endDate']
            
            cur=mysql.connection.cursor()

            orders = cur.execute("SELECT `typeID`, `quantity`, `startDate`, `endDate` FROM `productionplan` WHERE %s <= `startDate` AND %s >= `endDate`", [(startDate,), (endDate,)])

            if orders >0:
                orders = cur.fetchall()

            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal

    # Deletes an order with a specified "orderNumber"
    @app.route('/delete_order',methods=['DELETE'])
    def delete_order():
        
        if request.method == 'DELETE':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            delete_order = cur.execute("DELETE FROM `orders` WHERE `orderNumber`=%s", [(orderNumber,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()

            retVal = isAppropriate (Customer.endpoint , Customer.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal


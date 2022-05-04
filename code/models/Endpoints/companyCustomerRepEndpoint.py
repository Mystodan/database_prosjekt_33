from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class CustomerRep ():
  want = ep.ENDPOINT_EMPLOYEE.CUSTOMER_REPRESENTATIVE
  endpoint = ""
  def Route(app,mysql):
    # Retrieve all orders that have the specified value as their "state"
    @app.route('/get_state',methods=['GET'])
    def customer_rep_get_state():
        if request.method == 'GET':
            data = request.get_json()
            state=data['state']

            cur=mysql.connection.cursor()

            orders = cur.execute("SELECT * FROM `orders` WHERE `state`=%s",[(state,)])

            if orders > 0:
                orders = cur.fetchall()
            retVal = isAppropriate (CustomerRep.endpoint , CustomerRep.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal

    # Change the state of an order from "new" to "open"
    @app.route('/change_state_open',methods=['PUT'])
    def customer_rep_change_state_open():
        
        if request.method == 'PUT':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `orders` SET `state`='open' WHERE `orderNumber`=%s AND `state`='new'", (orderNumber,))
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (CustomerRep.endpoint , CustomerRep.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Change the state of an order from "open" to "available"
    @app.route('/change_state_available',methods=['PUT'])
    def customer_rep_change_state_available():
        
        if request.method == 'PUT':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `orders` SET `state`='available' WHERE `orderNumber`=%s AND `state`='open'",[(orderNumber,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (CustomerRep.endpoint , CustomerRep.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Fills an order and creates a shipment request for a shipment
    @app.route('/fill_order',methods=['POST'])
    def customer_rep_fill_order():
        
        if request.method == 'POST':
            data = request.get_json()
            transporterID=data['transporterID']
            orderNumber=data['orderNumber']
            shippingAddress=data['shippingAddress']
            pickUpDate=data['pickUpDate']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `orders` SET `state`='shipped' WHERE `orderNumber`=%s AND `state`='ready'", (orderNumber,))

            add_shipment = cur.execute("INSERT INTO `shipment` (`transporterID`, `orderNumber`, `shippingAddress`, `pickUpDate`, `state`) VALUES (%s, %s, %s, %s, 'ready')", ((transporterID,), (orderNumber,), (shippingAddress,), (pickUpDate,)))
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (CustomerRep.endpoint , CustomerRep.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal
  


from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class StoreKeeper ():
  want = ep.ENDPOINT_EMPLOYEE.STOREKEEPER
  endpoint = ""
  def Route(app,mysql):
    # Retrieve all skis that have the state "available"
    @app.route('/get_available',methods=['GET'])
    def get_available():
        
        if request.method == 'GET':
            
            cur=mysql.connection.cursor()

            orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'available'")

            if orders >0:
                orders = cur.fetchall()
            retVal = isAppropriate (StoreKeeper.endpoint , StoreKeeper.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal

    # Change the info of a newly made ski type
    @app.route('/change_info',methods=['PUT'])
    def change_info():
        
        if request.method == 'PUT':
            data = request.get_json()
            typeID=data['typeID']
            info=data['info']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `skitype` SET `description`=%s WHERE `typeID`=%s", [(info,), (typeID,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `skitype`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (StoreKeeper.endpoint , StoreKeeper.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Changes the state of an order to from "available" to "ready"
    @app.route('/change_state_ready',methods=['PUT'])
    def cancel_order():
        
        if request.method == 'PUT':
            data = request.get_json()
            orderNumber=data['orderNumber']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `orders` SET `state`='ready' WHERE `orderNumber`=%s AND `state`='available'", [(orderNumber,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `orders`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (StoreKeeper.endpoint , StoreKeeper.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

    # Creates a new record for newly produced skis
    @app.route('/create_record',methods=['POST'])
    def create_record():
        
        if request.method == 'POST':
            data = request.get_json()
            typeID=data['typeID']
            length=data['length']
            reserved=data['reserved']
            
            cur=mysql.connection.cursor()

            add_order = cur.execute("INSERT INTO `ski` (`typeID`, `length`, `reserved`) VALUES (%s, %s, %s)", [(typeID,),(length,),(reserved,)])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `ski`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (StoreKeeper.endpoint , StoreKeeper.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal

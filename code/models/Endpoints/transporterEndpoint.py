from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class Transporter ():
  want = ep.ENDPOINT_TRANSPORTER
  endpoint = ""
  def Route(app,mysql):
    # Retrieve all orders that have the state "ready"
    @app.route('/get_ready',methods=['GET'])
    def transporter_get_ready():
        
        if request.method == 'GET':
            
            cur=mysql.connection.cursor()

            orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'ready'")

            if orders >0:
                orders = cur.fetchall()

            retVal = isAppropriate (Transporter.endpoint , Transporter.want, (jsonify(orders),http.StatusCreated)) 
            cur.close()
            return retVal

    # Change the state of a shipment when it is picked up
    @app.route('/picked_up',methods=['PUT'])
    def transporter_picked_up():
        
        if request.method == 'PUT':
            data = request.get_json()
            shipmentNumber=data['shipmentNumber']
            
            cur=mysql.connection.cursor()

            change_state = cur.execute("UPDATE `shipment` SET `state`='shipped' WHERE `shipmentNumber`=%s", [(shipmentNumber),])
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `shipment`")

            if change_info > 0:
                change_info = cur.fetchall()

            retVal = isAppropriate (Transporter.endpoint , Transporter.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal
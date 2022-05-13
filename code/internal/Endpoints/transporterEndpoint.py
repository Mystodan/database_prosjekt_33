from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from internal.common import PreprocessEndpoint,setMethods


class Transporter ():
  """class handler for Transporter Endpoint
  """
  want = ep.ENDPOINT_TRANSPORTER
  endpoint = ""
  def Route(app,mysql):
    """Routes Transporter Endpoint

    Args:
        app (Flask): Application to route enpoints to
        mysql (_type_): Database to get data from

    Returns:
        _type_: body and status code
    """
    # Retrieve all orders that have the state "ready"
    @app.route('/get_ready',methods=setMethods())
    def transporter_get_ready(): return PreprocessEndpoint(Transporter,Transporter.get_ready, 'GET', mysql)

    # Change the state of a shipment when it is picked up
    @app.route('/picked_up',methods=setMethods())
    def transporter_picked_up(): return PreprocessEndpoint(Transporter,Transporter.picked_up, 'PUT', mysql)
  
  
  def get_ready(mysql) :         
    cur=mysql.connection.cursor()

    orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'ready'")

    if orders >0:
        orders = cur.fetchall()

    cur.close()
    return jsonify(orders),http.StatusCreated
          
  def picked_up(mysql):
    data = request.get_json()
    shipmentNumber=data['shipmentNumber']
    
    cur=mysql.connection.cursor()

    change_state = cur.execute("UPDATE `shipment` SET `state`='shipped' WHERE `shipmentNumber`=%s", [(shipmentNumber),])
    mysql.connection.commit()

    change_info = cur.execute("SELECT * FROM `shipment`")

    if change_info > 0:
        change_info = cur.fetchall()

    cur.close()
    return jsonify(change_info),http.StatusCreated
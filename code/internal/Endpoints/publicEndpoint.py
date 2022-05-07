from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep



class Public ():
  want = ep.ENDPOINT_PUBLIC
  endpoint = ""
  def Route(app,mysql):
    # Retrieve all ski types or all skis of a specified model.
    @app.route('/get_model',methods=['GET'])
    def public_get_model(): return Public.get_model(mysql)
   
   
  def get_model(mysql) :
    if request.method == 'GET':
      data = request.get_data()
      order = "SELECT skitype.*, ski.length FROM `skitype`, `ski`"
      cur=mysql.connection.cursor()
      noParams = False
      if data : 
        data = request.get_json()
        if data :
          model = data['model']
          order = order + "WHERE skitype.model = %s"
          exec = [(model,)]
          if len(data) == 2 :
            length = data['length']
            order = order + " AND ski.length = %s"
            exec = [(model,),(length,)]
          orders = cur.execute(order, exec)
        
        else : noParams = True
      else :
        noParams = True
      if noParams :
        orders = cur.execute(order,)
      if orders > 0:
          orders = cur.fetchall()

      cur.close()
      return jsonify(orders),http.StatusOk


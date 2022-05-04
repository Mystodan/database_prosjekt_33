from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class Public ():
  want = ep.ENDPOINT_PUBLIC
  endpoint = ""
  def Route(app,mysql):
    # Retrieve all ski types or all skis of a specified model.
    @app.route('/get_model',methods=['GET'])
    def get_model():
      if request.method == 'GET':
          data = request.get_data()
          order = "SELECT skitype.*, ski.length FROM `skitype`, `ski`"
          noPar = False
          cur=mysql.connection.cursor()
          if len(data) > 0 : 
            data = request.get_json()
            print(len(data))
            if len(data) > 0 :
              model = data['model']
              order = order + "WHERE skitype.model = %s"
              exec = [(model,)]
              if len(data) == 2 :
                length = data['length']
                order = order + " AND ski.length = %s"
                exec = [(model,),(length,)]
              orders = cur.execute(order, exec)
            
            else : noPar = True
          else :
            noPar = True
          if noPar :
            orders = cur.execute(order,)
          if orders > 0:
              orders = cur.fetchall()

 
          retVal = isAppropriate (Public.endpoint , Public.want, (jsonify(orders),http.StatusCreated)) 
          cur.close()
          return retVal


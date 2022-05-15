from flask import request, jsonify
from internal.common import setMethods, InvalidMethod, contains
from constants.REST import http,constantEndpoints as ep



class Public ():
  """class handler for Public Endpoint
  """
  want = ep.ENDPOINT_PUBLIC
  endpoint = ""
  def Route(app,mysql):
    """Routes Public Endpoint

    Args:
        app (Flask): Application to route enpoints to
        mysql (_type_): Database to get data from

    Returns:
        _type_: body and status code
    """
    # Retrieve all ski types or all skis of a specified model.
    @app.route('/get_model',methods=setMethods())
    def public_get_model(): return Public.get_model(mysql)
   
# functions which retrieves all ski types or all skis of a specified model.  
  def get_model(mysql) :
    wantedMethod = 'GET'
    if request.method == wantedMethod:
      data = request.get_data()
      order = "SELECT skitype.*, ski.length FROM `skitype`, `ski`"
      cur=mysql.connection.cursor()
      noParams = False
      t = data.replace(b'\r\n',b'')
      if contains(b'{', data) and contains(b'}', data): # set to ignore all other input than JSON
        print(t)
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
    else: return InvalidMethod(wantedMethod)

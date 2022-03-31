from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="ski_equipment_manufacturer"

mysql = MySQL(app)

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

        print(order, len(data))
        cur.close()
        return jsonify(orders),201

if __name__ == '__main__':
    app.run(debug=True)
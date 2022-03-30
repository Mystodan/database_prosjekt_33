from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="ski_equipment_manufacturer"

mysql = MySQL(app)

@app.route('/')
def index():
    return "Hello"

# Retrieve all orders that have the state "ready"
@app.route('/get_ready',methods=['GET'])
def get_ready():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'ready'")

        if orders >0:
            orders = cur.fetchall()

        cur.close()
        return jsonify(orders),201

# Change the state of a shipment when it is picked up
@app.route('/picked_up',methods=['POST'])
def picked_up():
    
    if request.method == 'POST':
        data = request.get_json()
        shipmentNumber=data['shipmentNumber']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `shipment` SET `state`='shipped' WHERE `shipmentNumber`=%s", [shipmentNumber])
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `shipment`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

if __name__ == '__main__':
    app.run(debug=True)
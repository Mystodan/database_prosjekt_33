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

# Retrieve all orders that have the specified value as their "state"
@app.route('/get_state',methods=['GET'])
def get_state():
    
    if request.method == 'GET':

        data = request.get_json()
        state=data['state']

        cur=mysql.connection.cursor()

        orders = cur.execute("SELECT * FROM `orders` WHERE `state`=%s",[(state,)])

        if orders > 0:
            orders = cur.fetchall()

        cur.close()
        return jsonify(orders),201

# Change the state of an order from "new" to "open"
@app.route('/change_state_open',methods=['PUT'])
def change_state_open():
    
    if request.method == 'PUT':
        data = request.get_json()
        orderNumber=data['orderNumber']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`='open' WHERE `orderNumber`=%s AND `state`='new'", (orderNumber,))
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

# Change the state of an order from "open" to "available"
@app.route('/change_state_available',methods=['PUT'])
def change_state_available():
    
    if request.method == 'PUT':
        data = request.get_json()
        orderNumber=data['orderNumber']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`='available' WHERE `orderNumber`=%s AND `state`='open'",(orderNumber,))
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

# Fills an order and creates a shipment request for a shipment
@app.route('/fill_order',methods=['POST'])
def fill_order():
    
    if request.method == 'POST':
        data = request.get_json()
        transporterID=data['transporterID']
        orderNumber=data['orderNumber']
        customerID=data['customerID']
        shippingAddress=data['shippingAddress']
        pickUpDate=data['pickUpDate']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`='shipped' WHERE `orderNumber`=%s AND `state`='ready'", (orderNumber,))

        add_shipment = cur.execute("INSERT INTO `shipment` (`transporterID`, `orderNumber`, `customerID`, `shippingAddress`, `pickUpDate`, `state`) VALUES (%s, %s, %s, %s, %s, 'ready')", ((transporterID,), (orderNumber,), (customerID,), (shippingAddress,), (pickUpDate,)))
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

if __name__ == '__main__':
    app.run(debug=True)
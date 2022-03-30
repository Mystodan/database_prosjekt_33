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

# Retrieve all skis that have the state "available"
@app.route('/get_orders',methods=['GET'])
def get_orders():
    
    if request.method == 'GET':
        data = request.get_json()
        customerID=data['customerID']
        cur=mysql.connection.cursor()
        order = "SELECT shipment.* FROM `shipment`, `customer` WHERE shipment.customerID =%s AND customer.customerID = shipment.customerID"
        exec = [(customerID,)]
        
        if len(data) == 2 :
          since=data['since']
          order = order + " AND customer.startDate = %s"
          exec = [(customerID,),(since,)]
  
        orders = cur.execute(order, exec)
        
        if orders >0:
            orders = cur.fetchall()
        cur.close()
        return jsonify(orders),201



# Retrieve all skis that have the state "available"
@app.route('/get_order_info',methods=['GET'])
def get_order_info():
    
    if request.method == 'GET':
        data = request.get_json()
        shipmentNumber=data['shipmentNumber']
        
        cur=mysql.connection.cursor()

        orders = cur.execute("SELECT * FROM `shipment` WHERE `shipmentNumber`=%s", [(shipmentNumber,)])

        if orders >0:
            orders = cur.fetchall()

        cur.close()
        return jsonify(orders),201

# Fills an order and creates a shipment request for a shipment with the state "ready"
@app.route('/place_order',methods=['POST'])
def place_order():
    
    if request.method == 'POST':
        data = request.get_json()
        quantity=data['quantity']
        
        cur=mysql.connection.cursor()

        add_order = cur.execute("INSERT INTO `orders` (`quantity`, `state`) VALUES (%s, 'new')", [(quantity,)])
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

# Fills an order and creates a shipment request for a shipment with the state "ready"
@app.route('/cancel_order',methods=['POST'])
def cancel_order():
    
    if request.method == 'POST':
        data = request.get_json()
        orderNumber=data['orderNumber']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `orders` SET `state`='cancelled' WHERE `orderNumber`=%s", [(orderNumber,)])
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

# Retrieve all skis that have the state "available"
@app.route('/get_plan_summary',methods=['GET'])
def get_plan_summary():
    
    if request.method == 'GET':
        data = request.get_json()
        startDate=data['startDate']
        endDate=data['endDate']
        
        cur=mysql.connection.cursor()

        orders = cur.execute("SELECT `typeID`, `quantity`, `startDate`, `endDate` FROM `productionplan` WHERE %s <= `startDate` AND %s >= `endDate`", [(startDate,), (endDate,)])

        if orders >0:
            orders = cur.fetchall()

        cur.close()
        return jsonify(orders),201

if __name__ == '__main__':
    app.run(debug=True)
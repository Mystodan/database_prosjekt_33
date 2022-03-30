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
@app.route('/get_available',methods=['GET'])
def get_available():
    
    if request.method == 'GET':
        
        cur=mysql.connection.cursor()

        orders = cur.execute("SELECT * FROM `orders` WHERE `state`= 'available'")

        if orders >0:
            orders = cur.fetchall()

        cur.close()
        return jsonify(orders),201

# Change the info of a newly made ski type
@app.route('/change_info',methods=['POST'])
def change_info():
    
    if request.method == 'POST':
        data = request.get_json()
        typeID=data['typeID']
        info=data['info']
        
        cur=mysql.connection.cursor()

        change_state = cur.execute("UPDATE `skitype` SET `description`=%s WHERE `typeID`=%s", [(info,), (typeID,)])
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `skitype`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201


if __name__ == '__main__':
    app.run(debug=True)
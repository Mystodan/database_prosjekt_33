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

# Fills an production plan
@app.route('/fill_plan',methods=['POST'])
def fill_plan():
    
    if request.method == 'POST':
        data = request.get_json()
        employeeNumber=data['employeeNumber']
        startDate=data['startDate']
        endDate=data['endDate']
        typeID=data['typeID']
        
        cur=mysql.connection.cursor()

        add_plan = cur.execute("INSERT INTO `productionplan` (`employeeNumber`, `typeID`, `startDate`, `endDate`) VALUES (%s, %s, %s, %s)", (employeeNumber, typeID, startDate, endDate))
        mysql.connection.commit()

        change_info = cur.execute("SELECT * FROM `orders`")

        if change_info > 0:
            change_info = cur.fetchall()

        cur.close()
        return jsonify(change_info),201

if __name__ == '__main__':
    app.run(debug=True)
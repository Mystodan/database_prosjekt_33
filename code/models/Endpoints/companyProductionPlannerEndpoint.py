from flask import request, jsonify
from constants.REST import http,constantEndpoints as ep
from models.common import isAppropriate


class ProductionPlanner ():
  want = ep.ENDPOINT_EMPLOYEE.PRODUCTION_PLANNER
  endpoint = ""
  def Route(app,mysql):
    # Fills an production plan and adds it to the database
    @app.route('/fill_plan',methods=['POST'])
    def fill_plan():
        
        if request.method == 'POST':
            data = request.get_json()
            employeeNumber=data['employeeNumber']
            startDate=data['startDate']
            endDate=data['endDate']
            typeID=data['typeID']
            quantity=data['quantity']
            
            cur=mysql.connection.cursor()

            add_plan = cur.execute("INSERT INTO `productionplan` (`employeeNumber`, `typeID`, `startDate`, `endDate`, `quantity`) VALUES (%s, %s, %s, %s, %s)", ((employeeNumber,), (typeID,), (startDate,), (endDate,), (quantity,)))
            mysql.connection.commit()

            change_info = cur.execute("SELECT * FROM `productionplan`")

            if change_info > 0:
                change_info = cur.fetchall()
            retVal = isAppropriate (ProductionPlanner.endpoint , ProductionPlanner.want, (jsonify(change_info),http.StatusCreated)) 
            cur.close()
            return retVal


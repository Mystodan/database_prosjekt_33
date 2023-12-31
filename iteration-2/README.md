# Project group 33

**Members**: <br>
Daniel and Sang

### Dependencies 
Here are the dependencies for the project:
- <a href = https://www.postman.com/downloads/> Postman </a> for interracting with our database (ski_equipment_manufacturer)
- <a href = https://www.apachefriends.org/download.html > XAMPP </a> which includes *phpMyAdmin*
- <a href = https://www.python.org/downloads/> Python </a> or the <a href = https://www.anaconda.com/products/distribution>Anaconda package</a> which includes python
- An IDE, we used <a href = https://code.visualstudio.com/download> VSCODE </a>
- <a href = https://git-scm.com/downloads> Git bash package</a>

### Modules
Here are the required modules required to run the python code<br><br>
**IMPORTANT** `⬇`

![env_activation.png](./images/env_activation.png)

> Remember to **activate** your environment before installing the modules so that the environment gets the required modules<br>

![images/python_env.png](./images/python_env.png)

> Remember to set the environment as the preferred python compiler f.ex. `3.10.4 (virt_env': venv)`
#### Required modules
- flask
- flask_mysqldb

##### Installing required modules
Use `pip install` and then the required module name
> for example: `pip install flask`

## How to use...


0.  Activate Apache and MySQL in XAMPP.
    - Use http://localhost/phpmyadmin/ to access phpMyAdmin
1.  Download the SQL file and import it into phpMyAdmin. <br>
    - Here is the required database (ski_equipment_manufacturer) <a href = https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/sangnn/project-group-33/-/blob/main/iteration-2/data/ski_equipment_manufacturer.sql>SQL file </a>
2.  Download the project code (<a href = https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/sangnn/project-group-33/-/tree/main/code>these </a> are the different endpoints). <br>
3.  Run the environment script in VS Code and then run the different endpoints you want to test. <br>
    - Heres a <a href = https://docs.python.org/3/library/venv.html>link</a> in order to setup environment
    - check out **required modules**`⬆` for setting up the environment
4.  In Postman you can add a body (JSON-format) with extra information as the input for some of different functions (some functions does not require this). <br>

![activateXAMPP.png](./images/activateXAMPP.png)<br>
(Heres how to activate Apache and MySQL)
### Importing databases
![navigatePHP.png](./images/navigatePHP.png)

> Navigate to the phpMyAdmin button on the dashboard tabs 
<br>
<br>
![navigateImport.png](./images/navigateImport.png)

> Navigate to the import button on the phpMyAdmin tabs and press the choose file option
<br>
<br>
![SQLpick.png](./images/SQLpick.png)

> Navigate to \project-group-33\data and input the database

## Verified users
Auth_token	: "Customer"        <br>
Password	:                   <br>

Auth_token	: "Transporter"     <br>
Password	:                   <br>

Auth_token	: "Prod_planner"    <br>
Password	: "admin"           <br>

Auth_token	: "Storekeeper"     <br>
Password	: "admin"           <br>

Auth_token	: "Customer_rep"    <br>
Password	: "admin"           <br>


<br>
<br>
<br>

## Example of endpoints
> Testing these endpoints can be done by hitting the copy button next to the previewed code and pasting it onto the body section of postman<br>
> **!!** - remember that the url is case sensitive, and when copying the url any spaces after the url would likely lead to a **404** - Not found error.

#### Authentication
METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/login <br>
            Body (raw, JSON): <br>

    {  
    "auth_token": "Transporter" 
    } 
Case **optional parameters**: <br>

    {  
    "auth_token": "storekeeper" ,
    "password": "admin"
    } 

>Output:     Login text based on if authenticated. <br>

METHOD:     **POST** (*optional parameters*) <br>
URL:        http://127.0.0.1:5000/get_model <br>


>Output:     Retrieve all skis that have the model "active". <br>


#### Public 
METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_model <br>
>Output:     All available ski types will be retrieved (with optional model name filter). <br>

METHOD:     **GET** (*optional parameters*) <br>
URL:        http://127.0.0.1:5000/get_model <br>
            Body (raw, JSON): <br>

    {  
    "model": "active",  
    "length": "152"
    } 

>Output:     Retrieve all skis that have the model "active". <br>

#### Storekeeper
METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/employee/get_available <br>
>Output:     Retrieve all skis that have the state "available". <br>

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/employee/change_info <br>
            Body (raw, JSON): 

    {
    "info": "Test 123",
    "typeID": "1"
    }
>Output:    Change the info (description) of a newly made ski type (typeID: 1) to "Test 123"

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/employee/change_state_ready <br>
            Body (raw, JSON): 

    {
    "orderNumber": "4"
    }
>Output:    Changes the state of order 4 from "available" to "ready"

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/employee/create_record <br>
            Body (raw, JSON): 

    {
    "typeID": "1",
    "length": "147",
    "reserved": "0"
    }
>Output:    Creates a new record for a newly produced ski with the data from JSON

#### Customer
METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_orders <br>
            Body (raw, JSON): 

    {  
    "customerID": "1"
    } 
>Output:    Retrieves a list of orders a customer has made "1"  <br>

METHOD:     **GET** (*optional parameters*) <br>
URL:        http://127.0.0.1:5000/get_orders <br>
            Body (raw, JSON): 
            
    { 
    "customerID": "2", 
    "since": "22-03-13"
    } 
>Output:    Retrieves a list of orders a customer has made (with an optional since filter)  <br>

METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_plan_summary <br>
            Body (raw, JSON): 

    {  
    "startDate": "2022-06-10", 
    "endDate": "2022-08-29"  
    } 
>Output:     Get the production plans that are ongoing between the specified startDate and endDate <br>

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/delete_order <br>
            Body (raw, JSON): 
            
    {  
    "orderNumber": "100"  
    } 
>Output:     Delete the order that has the order_number equal to 100. <br>

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/cancel_order <br>
            Body (raw, JSON): 
   
    {  
    "orderNumber": "200" 
    } 
>Output:     Change the state of an order with the "orderNumber" equal to 200 to "cancelled". <br>

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/place_order <br>
            Body (raw, JSON): 

    {
    "customerID": "1",
    "quantity": "999"
    }
>Output:    Creates a new order for "customerID: 1" and with "quantity: 999"

METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_order_info <br>
            Body (raw, JSON): 

    {
    "orderNumber": "2",
    }
>Output:    Retrieve all information and its state for "orderNumber: 2"

#### Customer representative

METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/employee/get_state  <br>
            Body (raw, JSON): 
            
    {  
    "state": "new"  
    } 
>Output:     Retrieve a list of all orders with the state equal to "new". <br>

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/employee/change_state_open <br>
            Body (raw, JSON): 

    {  
    "orderNumber": "1"
    } 
>Output:    Changes the "state" of an order from "new" to "open"

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/employee/change_state_available <br>
            Body (raw, JSON): 

    {  
    "orderNumber": "1"
    } 
>Output:    Changes the "state" of an order from "open" to "available"

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/employee/fill_order <br>
            Body (raw, JSON): 

    {
    "transporterID": "2",
    "orderNumber": "3",
    "shippingAddress": "Bokveien 5",
    "pickUpDate": "29-04-2022"
    }
>Output:    Fills an order and creates a shipment request for a shipment

#### Production planner

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/employee/fill_plan <br>
            Body (raw, JSON): 

    {
    "employeeNumber": "2",
    "typeID": "1",
    "quantity": "2000",
    "startDate": "2023-01-01",
    "endDate": "2023-01-29"
    }
>Output:    Fills an production plan with data from JSON and adds it to the database

#### Transporter

METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_ready <br>
>Output:    Retrieve all orders that have the state "ready"

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/picked_up <br>
            Body (raw, JSON): 

    {
    "shipmentNumber": "1"
    }
>Output:    Change the state of "shipmentNumber: 1" from "ready" to "shipped" once picked up


#### Testing
Testing was done within the <a href = https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/sangnn/project-group-33/-/tree/main/iteration-2/code/testing>testing folder </a>using the unittest, and requests library. 
> Testing would be improved if given more time

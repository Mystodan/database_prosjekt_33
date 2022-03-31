# Project group 33

**Members**: <br>
Daniel and Sang



## How to use...
0.  Activate Apache and MySQL in XAMPP.
    - Use http://localhost/phpmyadmin/ to access phpMyAdmin
1.  Download the SQL file and import it into phpMyAdmin. <br>
    - Here is the required database <a href = https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/sangnn/project-group-33/-/blob/main/data/ski_equipment_manufacturer.sql>SQL file </a>
2.  Download the project code (<a href = https://git.gvk.idi.ntnu.no/course/idatg2204/idatg2204-2022-workspace/sangnn/project-group-33/-/tree/main/code>these </a> are the different endpoints). <br>
3.  Run the environment script in VS Code and then run the different endpoints you want to test. <br>
    - Heres a <a href = https://docs.python.org/3/library/venv.html>link</a> in order to setup environment
    - check out **required modules**`⬇` for setting up the environment
4.  In Postman you can add a body (JSON-format) with extra information as the input for some of different functions (some functions does not require this). <br>
### Modules
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

<br>
<br>
<br>

## Example of endpoints
> Testing these endpoints can be done by hitting the copy button next to the previewed code and pasting it onto the body section of postman<br>
> **!!** - remember that when copying the url any spaces after the url would likely lead to a **404** - Not found error.
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
URL:        http://127.0.0.1:5000/get_available <br>
>Output:     Retrieve all skis that have the state "available". <br>

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

#### Customer representative

METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_state  <br>
            Body (raw, JSON): 
            
    {  
    "state": "new"  
    } 
>Output:     Retrieve a list of all orders with the state equal to "new". <br>

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/change_state_open <br>
            Body (raw, JSON): 

    {  
    "orderNumber": "1"
    } 
>Output:    Changes the "state" of an order from "new" to "open"

METHOD:     **PUT** <br>
URL:        http://127.0.0.1:5000/change_state_available <br>
            Body (raw, JSON): 

    {  
    "orderNumber": "1"
    } 
>Output:    Changes the "state" of an order from "open" to "available"

METHOD:     **POST** <br>
URL:        http://127.0.0.1:5000/fill_order <br>
            Body (raw, JSON): 

    {
    "transporterID": "2",
    "orderNumber": "3",
    "shippingAddress": "Bokveien 5",
    "pickUpDate": "29-04-2022"
    }
>Output:    Fills an order and creates a shipment request for a shipment

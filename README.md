# Project group 33

Members: <br>
Daniel and Sang

## Example of endpoints
#### Public 
METHOD:     **GET** <br>
URL:        http://127.0.0.1:5000/get_model <br>
>Output:     All available ski types will be retrieved (with optional model name filter). <br>

METHOD:     **GET** (*optional parameters*) <br>
URL:        http://127.0.0.1:5000/get_model <br>
            Body (raw, JSON): <br>

    {  # optional
    "model": "active"  
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
            
    { # optional
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
URL:        http://127.0.0.1:5000/cancel_order <br>
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







## How to use...
0. Activate Apache and MySQL in XAMPP.
1. Download the SQL file and import it into phpMyAdmin. <br>
2. Download the project code (these are the different endpoints). <br>
3. Run the environment script in VS Code and then run the different endpoints you want to test. <br>
4. In Postman you can add a body (JSON-format) with extra information as the input for some of different functions (some functions does not require this). <br>

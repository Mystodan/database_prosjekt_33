# Project group 33

Members: <br>
Daniel and Sang

## Example of endpoints
Endpoint:   Public <br>
METHOD:     GET <br>
URL:        http://127.0.0.1:5000/get_model <br>
Output:     All available ski types will be retrieved (with optional model name filter). <br>

Endpoint:   storekeeper <br>
METHOD:     GET <br>
URL:        http://127.0.0.1:5000/get_available <br>
Output:     Retrieve all skis that have the state "available". <br>

Endpoint:   customer <br>
METHOD:     POST <br>
URL:        http://127.0.0.1:5000/cancel_order <br>
            Body (raw, JSON): {  <br>
                "orderNumber": "100"  <br>
            } <br>
Output:     Delete the order that has the order_number equal to 100. <br>

Endpoint:   Public <br>
METHOD:     GET <br>
URL:        http://127.0.0.1:5000/get_model <br>
            Body (raw, JSON): {  <br>
                "model": "active"  <br>
            } <br>
Output:     Retrieve all skis that have the model "active". <br>

Endpoint:   customer_rep <br>
METHOD:     GET <br>
URL:        http://127.0.0.1:5000/get_state  <br>
            Body (raw, JSON): {  <br>
                "state": "new"  <br>
            } <br>
Output:     Retrieve a list of all orders with the state equal to "new". <br>

Endpoint:   customer <br>
METHOD:     GET <br>
URL:        http://127.0.0.1:5000/get_plan_summary <br>
            Body (raw, JSON): {  <br>
                "startDate": "2022-06-10", <br>
                "endDate": "2022-08-29"  <br>
            } <br>
Output:     Get the production plans that are ongoing between the specified startDate and endDate <br>

Endpoint:   customer <br>
METHOD:     PUT <br>
URL:        http://127.0.0.1:5000/cancel_order <br>
            Body (raw, JSON): {  <br>
                "orderNumber": "200" <br>
            } <br>
Output:     Change the state of an order with the "orderNumber" equal to 200 to "cancelled". <br>

## How to use...
0. Activate Apache and MySQL in XAMPP.
1. Download the SQL file and import it into phpMyAdmin. <br>
2. Download the project code (these are the different endpoints). <br>
3. Run the environment script in VS Code and then run the different endpoints you want to test. <br>
4. In Postman you can add a body (JSON-format) with extra information as the input for some of different functions (some functions does not require this). <br>

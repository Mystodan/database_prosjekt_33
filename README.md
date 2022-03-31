# Project group 33

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

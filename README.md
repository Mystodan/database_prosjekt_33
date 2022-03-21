# Project group 33

Daniel and Sang

## Example of endpoints
Endpoint:   Public <br>
METHOD:     GET <br>
URL:        localhost/api/products <br>
Output:     All available products will be retrieved <br>

Endpoint:   storekeeper <br>
METHOD:     POST <br>
URL:        localhost/api/products/create <br>
                Body (raw): {  <br>
                "msrp" : 420,  <br>
                "model" : "Redline",  <br>
                "type" : "Skate",  <br>
                "img_url" : "https://lmg.azureedge.net/images/upload/2021/02/24/IMG_0714.jpg?"  <br>
            } <br>
Output:     A new product will be added with different values for the attributes. <br>

Endpoint:   customer <br>
METHOD:     DELETE <br>
URL:        localhost/api/orders/69/delete <br>
Output:     Delete the order that has the order_number equal to 69. <br>

Endpoint:   Public <br>
METHOD:     GET <br>
URL:        localhost/api/products?model=Endurance&type=classic <br>
Output:     Availalbe products will be retrieved that is of the model "Endurance" and the type is "Classic". <br>

Endpoint:   customer_rep <br>
METHOD:     GET <br>
URL:        localhost/api/orders  <br>
Output:     Retrieve a list of all orders with the state equal to "new". <br>

Endpoint:   customer <br>
METHOD:     GET <br>
URL:        localhost/api/products/plan <br>
Output:     Skis that are still in the planning phase is retrieved. <br>

Endpoint:   customer_rep <br>
METHOD:     PUT <br>
URL:        localhost/api/orders/69/state=cancelled <br>
Output:     Change the state of order with the "orderNumber" equal to 69 to "cancelled". <br>

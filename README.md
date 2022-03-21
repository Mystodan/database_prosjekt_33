# Project group 33

Daniel and Sang

## Example of endpoints
Endpoint:   Public
METHOD:     GET
URL:        localhost/api/products
Output:     All available products will be retrieved

Endpoint:   storekeeper
METHOD:     POST
URL:        localhost/api/products/create
                Body (raw): { 
                "msrp" : 420, 
                "model" : "Redline", 
                "type" : "Skate", 
                "img_url" : "https://lmg.azureedge.net/images/upload/2021/02/24/IMG_0714.jpg?" 
            }
Output:     A new product will be added with different values for the attributes.

Endpoint:   customer
METHOD:     DELETE
URL:        localhost/api/orders/69/delete
Output:     Delete the order that has the order_number equal to 69.

Endpoint:   Public
METHOD:     GET
URL:        localhost/api/products?model=Endurance&type=classic
Output:     Availalbe products will be retrieved that is of the model "Endurance" and the type is "Classic".

Endpoint:   customer_rep
METHOD:     GET
URL:        localhost/api/orders 
Output:     Retrieve a list of all orders with the state equal to "new".

Endpoint:   customer
METHOD:     GET
URL:        localhost/api/products/plan
Output:     Skis that are still in the planning phase is retrieved.

Endpoint:   customer_rep
METHOD:     PUT
URL:        localhost/api/orders/69/state=cancelled
Output:     Change the state of order with the "orderNumber" equal to 69 to "cancelled".

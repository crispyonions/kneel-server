ORDERS = [
    {
        "id": 1, "customer": "John Smith",
        "items": [{"product": "Gold Ring", "metal": "Gold", "style": "Classic", "size": "Medium", "quantity": 1},
        {"product": "Silver Necklace", "metal": "Silver", "style": "Modern", "size": "Large", "quantity": 2}],
        "total": 375.0
    },
    {
        "id": 2,
        "customer": "Jane Doe",
        "items": [{"product": "Platinum Bracelet", "metal": "Platinum", "style": "Vintage", "size": "Small", "quantity": 1}],
        "total": 400.0
    }
]

def get_all_orders():
    return ORDERS

# Function with a single parameter
def get_single_order(id):
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # Add an `id` property to the order dictionary
    order["id"] = new_id
    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the orderS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index
    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:      
        ORDERS.pop(order_index)
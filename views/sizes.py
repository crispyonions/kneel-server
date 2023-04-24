SIZES= [
    {
    "id":1,
    "name":"Small",
    "description":"Fits wrist circumference up to 6.5 inches.",
    "price":0.0
    },
    {
    "id":2,
    "name":"Medium",
    "description":"Fits wrist circumference from 6.5 to 7.5 inches.",
    "price":0.0
    },
    {
    "id":3,
    "name":"Large",
    "description":"Fits wrist circumference from 7.5 to 8.5 inches.",
    "price":0.0
    }
]

def get_all_sizes():
    return SIZES

# Function with a single parameter
def get_single_size(id):
    # Variable to hold the found size, if it exists
    requested_size = None

    # Iterate the sizeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for size in SIZES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if size["id"] == id:
            requested_size = size

    return requested_size

def create_size(size):
    # Get the id value of the last size in the list
    max_id = SIZES[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # Add an `id` property to the size dictionary
    size["id"] = new_id
    # Add the size dictionary to the list
    SIZES.append(size)

    # Return the dictionary with `id` property added
    return size

def delete_size(id):
    # Initial -1 value for size index, in case one isn't found
    size_index = -1

    # Iterate the sizeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            # Found the size. Store the current index.
            size_index = index
    # If the size was found, use pop(int) to remove it from list
    if size_index >= 0:      
        SIZES.pop(size_index)
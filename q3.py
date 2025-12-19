def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    return

def update_dictionary(dct, key, value):

    if not isinstance(dct, dict):
        return -1
    if key in dct:
        print(dct[key])
    dct[key] = value
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:

# - {}, "name", "Alice"
   update_dictionary({}, "name", "Alice")
    -> returns: {'name': 'Alice'} (no printed original value)

# - {"age": 25}, "age", 26
    update_dictionary({"age": 25}, "age", 26)
    -> prints: 25
    -> returns: {'age': 26}

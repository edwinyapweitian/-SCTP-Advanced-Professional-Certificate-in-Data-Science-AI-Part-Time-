def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return

    # Check if both variables are numeric
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        # Swap values
        x, y = y, x
        print(x, y)  # Print swapped values
        return
    else:
        # Return -1 for non-numeric inputs
        return -1

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
swap("Apple", 10)
# Output: -1

# - 9, 17
swap(9, 17)
# Output: 17 9

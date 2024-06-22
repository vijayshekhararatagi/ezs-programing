def find_smallest_positive_integer(numbers):
    # Filter out positive integers from the list
    positive_numbers = [num for num in numbers if num > 0]
    
    # Check if there are any positive integers in the list
    if not positive_numbers:
        return None  # Return None if there are no positive integers
    
    # Find and return the smallest positive integer
    return min(positive_numbers)

# Take user input
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = list(map(int, user_input.split()))

# Find the smallest positive integer
smallest_positive_integer = find_smallest_positive_integer(numbers)

# Print the result
if smallest_positive_integer is not None:
    print("The smallest positive integer is:", smallest_positive_integer)
else:
    print("There are no positive integers in the input.")


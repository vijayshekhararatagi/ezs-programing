def count_commas(input_value):
    # Convert the input to a string if it is not already a string
    if not isinstance(input_value, str):
        input_value = str(input_value)
    # Count the number of commas in the string
    return input_value.count(',')

# Take user input
user_input = input("Enter a string or number: ")

# Try to convert the user input to an integer, if possible
try:
    user_input = int(user_input)
except ValueError:
    pass  # If conversion fails, treat the input as a string

total_commas = count_commas(user_input)

print("The total number of commas in the given input is:", total_commas)

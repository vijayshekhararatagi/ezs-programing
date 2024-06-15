def min_key_presses(target):
    presses = 0
    number = int(target)
    
    while number > 0:
        # If the last two digits are 00 and the number is greater than 100, press '00'
        if number % 100 == 0 and number >= 100:
            number //= 100
            presses += 1
        else:
            # Otherwise, divide by 10 and press the corresponding key
            presses += 1
            number //= 10
    
    return presses

# Example usage:
target_number = "500"
print(f"Minimum key presses to reach {target_number}: {min_key_presses(target_number)}")

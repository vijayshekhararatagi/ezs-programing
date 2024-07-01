def operations_binary_string(binary_str):
    if binary_str is None or len(binary_str) == 0:
        return -1
    
   
    result = int(binary_str[0])
    
    i = 1
    while i < len(binary_str) - 1:
        operation = binary_str[i]
        next_digit = int(binary_str[i + 1])
        
        if operation == 'A':
            result = result & next_digit
        elif operation == 'B':
            result = result | next_digit
        elif operation == 'C':
            result = result ^ next_digit
        
        i += 2
    
    return result

print(operations_binary_string("1C0C1C1A0B1"))  
print(operations_binary_string("0C1A1B1C1C1B0A0"))
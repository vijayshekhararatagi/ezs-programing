def find_substring_indices(S, P):
    indices = []
    start = 0  # Initialize the starting position for the search
    
    while True:
        # Find the next occurrence of P in S starting from 'start'
        index = S.find(P, start)
        
        if index == -1:  # If no more occurrences are found, break the loop
            break
        
        indices.append(index)  # Append the found index to the list
        start = index + 1  # Update the starting position for the next search
    
    return indices

# Example usage
S = "ADDCMABABABCANFDKABAABCNCKABABCACNDA"
P = "ABABCA"
indices = find_substring_indices(S, P)
print("The indices of 'P' in 'S' are:", indices)

def roman_to_int(s):
    s_length = len(s)
    
    # Invalid length
    if s_length < 1 or s_length > 15:
        return None
    
    # Assuming that the string is a valid roman numeral string
    mappings = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    result = 0
    
    for i in range(s_length):
        # Getting the current number
        curr_num = mappings[s[i]]
        next_num = 0 if i == s_length - 1 else mappings[s[i + 1]]
        
        if curr_num < next_num:
            result -= curr_num
        else:
            result += curr_num
    
    return result

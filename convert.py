def roman_to_int(s):
    """
    Converts a Roman numeral string to an integer.
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1 or roman_dict[s[i]] >= roman_dict[s[i+1]]:
            total += roman_dict[s[i]]
            i += 1
        else:
            total += roman_dict[s[i+1]] - roman_dict[s[i]]
            i += 2
    return total

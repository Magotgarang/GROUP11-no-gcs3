phrase = input("Enter a phrase: ").lower()

chars_in_phrase = len(phrase)
count = 0
output = []

while count < chars_in_phrase:
    char = phrase[count]
    
    # Check if char is lowercase letter
    # This filters out symbols, numbers spaces etc
    if char >= 'a' and char <= 'z':
        # Check if char is not a variable
        if not (char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y"):
            output.append(char)
    
    count += 1

print(", ".join(output))

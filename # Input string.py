# Input string
string = input("Enter a string: ")

# Get the first character of the string
first_char = string[0]

# Replace all occurrences of the first character (except the first one) with '$'
modified_string = first_char + string[1:].replace(first_char, '$')

# Output the modified string
print("Modified string:", modified_string)

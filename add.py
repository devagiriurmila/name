number = input("Enter a number: ")
sum_digits = 0
for digit in number:
    if digit.isdigit():
        sum_digits += int(digit)
print("Sum of digits:", sum_digits)

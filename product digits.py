number = input("Enter a number: ")
product_digits = 1
for digit in number:
    if digit.isdigit():
        product_digits *= int(digit)
print("Product of digits:", product_digits)

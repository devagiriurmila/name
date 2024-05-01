# Input the number
number = int(input("Enter a number: "))

# Display the multiplication table for the given number up to 10
for i in range(1, 11):
    print(number, "X", i, "=", number * i)

# Input list of numbers
numbers = [2, 7, 5, 64, 14]

# Initialize variables to store the sum of even and odd numbers
even_sum = 0
odd_sum = 0

# Iterate through the numbers in the list
for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Output the sums
print("Even Sum =", even_sum)
print("Odd Sum =", odd_sum)

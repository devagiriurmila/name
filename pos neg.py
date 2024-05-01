# Input list of numbers
numbers = [ 2,-7,5,-64,-14 ]

# Initialize variables to store the count of positive and negative numbers
positive_count = 0
negative_count = 0

# Iterate through the numbers in the list
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

# Output the counts
print("Positive count =", positive_count)
print("Negative count =", negative_count)

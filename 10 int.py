def find_multiples_of_2_and_8(numbers):
    multiples_of_2_and_8 = [num for num in numbers if num % 2 == 0 and num % 8 == 0]
    return multiples_of_2_and_8

# Read 10 integer numbers
input_numbers = []
print("Enter 10 integer numbers:")
for _ in range(10):
    num = int(input())
    input_numbers.append(num)

# Find multiples of both 2 and 8
multiples = find_multiples_of_2_and_8(input_numbers)

# Display the result
print("Numbers that are multiples of both 2 and 8:")
print(multiples)
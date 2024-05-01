numbers = [12, 4, 3, 4, 6, 7, 100, 18, 2, 18, 18]
output=[]
for num in numbers:
    if numbers.count(num)==1:
        output.append(num)
print("output:",*output)
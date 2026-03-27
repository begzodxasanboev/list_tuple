import os
os.system('cls')

numbers = [1,2,3,4]
string1 ="emp"

for i in range(4):
    numbers.append(f"{string1}{numbers[i]}")
del numbers[:4]
print(numbers)
import os
os.system('cls')

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(tuples)
for i in range(3):
    tuples[i]=list(tuples[i])
    tuples[i][-1]=100
    tuples[i] = tuple(tuples[i])

print(tuples)

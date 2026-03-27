import os 
os.system('cls')

a = int(input('A='))
b = int(input('B='))
juftlar = []

for i in range(a,b):
    if i%2==0:
        juftlar.append(i)
print(juftlar)



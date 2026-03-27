import os
os.system('cls')

matn = input('Sozni kiriting: ')
t = []
uzinlik = len(matn)

for i in range(0,uzinlik):
    t.append(matn[i])
t=tuple(t)
print(t)


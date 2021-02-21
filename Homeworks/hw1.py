a = 0
liste = []
matrixa = []
matrixb = []
matrixc = []
matrix = []

import random

while (a < 9):
    sayi = random.randint(2, 100)
    asal = True
    for i in range(2, sayi):
        if (sayi % i) == 0:
            asal = False
            break
    if asal == True and sayi not in liste:
        liste.append(sayi)
        a += 1

matrixa.append(liste[0:3])
matrixb.append(liste[3:6])
matrixc.append(liste[6:9])

matrix = matrixa, matrixb, matrixc
print (matrix)
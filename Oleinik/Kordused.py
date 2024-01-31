     # 1
while True:
    maja = int(input("Sisestage kui palju maja te tahate (1-9): "))

    if 1 <= maja <= 9:
        break
    else:
        print("Sisestage arv vahemikus 1 kuni 9")

for i in range(maja):
    print(" ~~~~~")
    print("/_____\ ")
    print("| []  |")
    print(" -----")


     # 2
import math
hinned1 = [2,3,3,4,5,2,3,4,5,3,5,5,5,5,3,4,5,1,1,2,3,4]
hinned2 = [1,1,1,2,3,4,5,5,5,5,4,3,3,3,3,4,4,4,4,4,5,5]




     #3
from random import*
import random
õpilased = 22
maksimaalne = 1
minimaalne = 5
for i in range(õpilased):
    hinned = random.randint(100, 500)/100
    print(hinned)
    if hinned > maksimaalne:
        maksimaalne = hinned
    if hinned < minimaalne:
        minimaalne = hinned
print("Maksimaalne hind on::", maksimaalne)
print("Minimaalne hind on:", minimaalne)



    # 4
elanikkond = [120, 80, 150, 90, 110, 70, 130, 100, 140, 95, 120, 85]
pindala = [50, 30, 60, 40, 45, 25, 55, 35, 58, 38, 48, 33]
kogu_tihendus = 0
for i in range(len(elanikkond)):
    tihedus = elanikkond[i] / pindala[i]
    kogu_tihendus += tihedus

keskmine_tihendus = kogu_tihendus / len(elanikkond)

print(f"Piirkonna keskmine rahvastiku tihedus: {keskmine_tihendus} tuhat inimest/km^2")


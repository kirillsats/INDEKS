     # 1 немного исправил
while True:
    try:
        maja = int(input("Sisestage kui palju maja te tahate (1-9): "))
        if 1 <= maja <= 9:
            break
    except ValueError:
        print("Vale tuup")


for i in range(maja):
    print(" ~~~~~")
    print("/_____\ ")
    print("| []  |")
    print(" -----")


     # 2 исправлено
from random import *
N=25
kesk1=0
kesk2=0
for i in range(N):
    h1 = randint(1,5)
    h2 = randint(1,5)
    kesk1+=h1
    kesk2+=h2
kesk1/=N
kesk2/=N
print(f"Keskmine hinne esimeses klassis on {kesk1}")
print(f"Keskmine hinne teises klassis on {kesk2}")




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



    # 4 испрвлено
from random import *
sum_num = 0
sum_km = 0
for i in range(12):
    num = randint(1000, 100000)
    km = randint(1, 1000)
    sum_num+=num
    sum_km+=km
    print(f"{i}. maakond, Elanikud: \n{num}. Pindala: {km}\n Kokku: {sum_num}, \n{sum_km}")
vastus = sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")

 #4 вариант номер 5
from random import *
while True:
    try:
        K = int(input("Mitu kotleti sul on?"))
        if K>0: break
    except ValueError:
        print("Vale Tuup")
while True:
    try:
        M = int(input("Mitu kotleti uhel panil?"))
        if M>0: break
    except ValueError:
        print("Value tuup")
pann=0
while K>M:
    K-=M
    pann+=1
    print(f"Praetud: {pann} tk")
    if K<M:
        pann+=1
        print(f"Praetud: {pann} tk")
print(f"Kokku oli praetud: {pann} pannid")
print()


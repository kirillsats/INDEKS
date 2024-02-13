       # 1
from string import *
lause =input("Sisestage sõna või lause:").lower()
lause_list = list(lause)
vokaali = ["a", "e", "i", "o", "u", "ö", "ä", "õ", "ü" ]
v=k=m=t=0
konsonanti = ["b", "p", "d", "t", "g", "k", "s", "h", "f", "š", "z", "ž"]
markid = punctuation
for sümbool in lause_list:
    if sümbool in vokaali:
        v+=1
    elif sümbool in konsonanti:
        k+=1
    elif sümbool in markid:
        m+=1
    elif sümbool==" ":
        t+=1
print("vokaali:", v)
print("konsonanti:", k)
print("Kirjuvahemärgid:", m)
print("Tühikud:", t)



      # 2
nimed = []
for i in range(5):
    nimi = input("Sisesta nimed:")
    nimed.append(nimi)

print("Loetelu oli: ", nimed)
nimed.sort()
print( "Loetelu sorteeritud: ", nimed)
for n in range(len(nimed)):
    print(n+1,". ", nimed[n],sep="")
print("Vimasena oli lisatud: ", nimi)

uued_nimed = []
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

vanused = []
for n in range(5):
    vanus = input("Sisestage, kui vana sa oled: ")
    vanused.append(vanus)

maximum = max(vanused)
minimum = min(vanused)
print("Maksimum on: ",maximum)
print("Minimum on: ",minimum)
keskmine = (sum(vanused)) / (len(vanused))
print("Keskmine on: ",keskmine)

kokku = sum(vanused)
print(kokku)






# uued_nimed=list(set(nimed))

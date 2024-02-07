from random import *
nimed = ["Mati", "Meelis", "Kati", "Mati"]
while True:
    print("******************")
    v = input("N-näita andmed?\nL-lisada andmeid\nA-andmete kustutamine\nH-andmete haldus\nI-Positsiooni otsing\n")
    if v=="N":
        v = input("Kas juhuslik(j) nimi või terve loetele(t) ")
        if v=="t":
            print(nimed)
        elif v =="j":
            print(choice(nimed))
    elif v == "L":
        v = input("Kas nimekirja lõppu(l) või positsioonile(p)?")
        if v=="l":
            nimi = input("Sisestage oma nimi:")
            nimed.append(nimi)
        elif v == "p":
            ind=int(input("Mis kohale: "))
            nimed.insert(ind-1, nimi)
        elif v=="A":
            v = input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed?(k)")
            if v=="i":
                ind=int(input("Sisesta indeks:"))
                nimed.pop(ind-1)
            elif v=="k":
                nimed.clear()
            elif v=="n":
                nimi=input("Sisesta nimi: ")
                mitu = nimed.count(nimi)
                if mitu>0:
                    if mitu>1:
                        ind = -1
                        indlist = []
                        for e in nimed:
                            ind += 1
                            if e == nimi:
                                indlist.append(ind)
                        print(indlist)
                        v = int(input("Mis indeks?"))
                        nimed.pop(v)
                else:
                    nimed.remove(nimi)
            else:
                print(f"{nimi} ei ole loetelus")
            print( nimed,)
        elif v.lower() == "k":
            nimed.clear()
        elif v =="H":
            v=input("sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
            if v == "s":
                v=int(input("A-z? või Z-a(2)"))
                if v==1:
                    nimed.sort()
                elif v==2:
                    nimed.sort(reverse=True)
            elif v =="k":
                nimed.copy()
            elif v=="p":
                nimed.reverse()
            elif v =="I":
                nimi=input("Sisestage nimi:")
                mitu=nimed.count(nimi)
                if mitu>0:
                    print(f"Seal on {mitu} {nimi}")
                    for i in range(mitu):
                        print(f"{nimi} ei ole loetelus")
                        
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisestage oma nimi")
print("oi kui ilus nimi,",nimi)
indeks = int(input( "Kas leian Sinu keha indeksi? 0-ei, 1-jah =>: "))
if indeks==0:
    print("Ei")
if indeks==1:
    pikkus=int(input("Kirjutage teie pikkus"))
    mass=int(input("Kirjutage teie mass"))
    index=mass/(0.01*pikkus)**2
    print("Teie keha indeks on:", round(index, 1))
if index == 0 and index <16:
    print("Tervisele ohtlik alakaal")
elif index == 16 and index <19:
    print("Alakaal")
elif index == 19 and index <25:
    print("Normaalkaal")
elif index == 25 and index <30:
    print("Ülekaal")
elif index == 30 and index <35:
    print("Rasvumine")
elif index == 35 and index <40:
    print("Tugev rasvumine")
elif index >40:
    print("Tervisele ohtlik rasvumine ")
print("Kahju! See on väga kasulik info!")
print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

try:
    pikkus=int(input("Siseta oma kaal:"))
except:
    ValueError
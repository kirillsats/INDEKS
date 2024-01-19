# from random import *
#
# arv=randint(0,100)  #juhuslik raisarv vahemikust 0...100
# print(arv)
# if arv%2==0:
#     print(arv, "on paaris arv")
# else:
#     print(arv, "on paaritu arv")
# print()



# from random import *
# protsent=randint(-100, 500) #0-100   0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"
# print(protsent,"% on testi tulemus")
# if protsent<0 or protsent>100:
#     tulemus="Valed andmed"
# elif protsent>0 and protsent<60:
#     tulemus="hinne 2"
# elif protsent<=60 and protsent>75:
#     tulemus="hinne 3"
# elif protsent<=75 and protsent>90:
#     tulemus="hinne 4"
# elif protsent<=90 and protsent>=100:
#     tulemus="hinne 5"
# print(tulemus)

# print("tund on alanu")
# hilinemine=input("Kas õpilane on hilinenud?")
# # "JAH"-a.upper() ,"jah"-a.lower(), "Jah"-a.capitaliza(), jAH
# if hilinemine.upper()=="JAH":
#     print("Õpilane ootab 30 min")
# print("Õpilane astub klassi")

        #1
nimi = input("Mis on su nimi?").capitalize()
print("Tere,", nimi)
if nimi == "Juku":
    print("Lähme kinno")
    vanus=(input("Kui vana sa oled?"))
    vanus=int(vanus)
    if vanus<0 or vanus>100:
        pilet="Viga"
    elif vanus<=6:
        pilet="Tasuta"
    elif vanus<=14:
        pilet= "Lastepilet"
    elif vanus<65:
        pilet="taispilet"
    elif vanus<=100:
        pilet = "sooduspilet"
    print(pilet)
else:
    print("Ma ootan Jukut")



    #2
nimi = input("Mis on su nimi?")
if nimi == (nimi):
    nimi2 = input("Mis teie söber nimi on?")
if nimi2 == (nimi2):
    print("Täna te olete pinginaabrid")


    #3
from math import *
import math
pikkus = float(input("Sisestage pikkus:"))
laius = float(input("Sisestage laius:"))
S = pikkus*laius
print("Teie pindala on:", round(S,2))
vastus = input("Kas te tahate remondi teha? 0-ei, 1-jah =>:")
if vastus == "0":
    print("Head aega")
if vastus == "1":
    hind = float(input("Kui palju maksab ruutmeeter?"))
põrand = S*hind
print("Remondi hind on:", round(põrand, 2))

#     #4
alghind= float(input("Sisestage hind:"))
if alghind >= 700:
    soodus = 0.3
    soodushind = alghind* (1-soodus)
    print("Hind koos soodesustega :", round(soodushind,2))
else:
    print("Hind on väiksem kui 700")

      #5
temperatuur = float(int("Sisestage temperatuur:"))
if temperatuur >=18:
    print(f"Temperatuur on pikkem kui 18")
else:
    print(f"Temperatuur on vaiksem kui 18")



      #6

väikeinimene = 160
pikkinimene = 195
pikkus = float(input("Sisestage teie pikk: "))
if pikkus < väikeinimene:
    print("Madal pikk")
elif  väikeinimene <= pikkus < pikkinimene:
    print("Keskmine pikk")
else:
    print("Pikk pikkus")



      #7
vaikemees = 160
pikkmees = 195
vaikenaine = 140
pikknaine = 175
sugu1 = "mees"
sugu2 = "naine"
sugu = input("Sisestage teie sugu:")
pikkus = float(input("Sisestage teie pikk: "))
if sugu == "mees" and pikkus < vaikemees:
    print("Madal pikkus")
elif sugu == "mees" and vaikemees <= pikkus < pikkmees:
    print("Keskmine pikkus")
elif sugu == "mees" and pikkus >= pikkmees:
    print("Pikk pikkus")
elif sugu == "naine" and pikkus < vaikenaine:
    print("Madal pikkus")
elif sugu == "naine" and vaikenaine <= pikkus < pikknaine:
    print("Keskmine pikkus")
elif sugu == "naine" and pikkus >= pikknaine:
    print("Pikk pikkus")


#     #8
from datetime import *
from random import *
arve_nr = date.today()
print(arve_nr)
tsekk = "Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa = 0

toode = "Piim"
hind = randint(50,150)/100
v = input("Toode:"+toode+" Hind: "+str(hind)+"\nKas tahd osta?").lower()
if v == "jah":
    mitu = int(input("Mitu?"))
    tsekk += toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
    summa+=mitu*hind

toode = "Leib"
hind = randint(10, 100) / 100
v = input("Toode:" + toode + " Hind: " + str(hind) + "\nKas tahd osta?").lower()
if v == "jah":
    mitu = int(input("Mitu?"))
    tsekk += toode + " " + str(hind) + " " + str(mitu) + " " + str(mitu + hind) + "\n"
    summa += mitu * hind

toode = "Kommid"
hind = randint(90, 250) / 100
v = input("Toode:" + toode + " Hind: " + str(hind) + "\nKas tahd osta?").lower()
if v == "jah":
    mitu = int(input("Mitu?"))
    tsekk += toode + " " + str(hind) + " " + str(mitu) + " " + str(mitu + hind) + "\n"
    summa += mitu * hind
tsekk += "Kokku maksta: "+str(summa)
print(tsekk)
raha = float(input("Maksa "+str(summa)))
if raha == summa:
    print("Tanan ostu eest!")
elif raha>summa:
    print("Tana ostu eest! Tagasi " +str(raha-summa))
else:
    print("Makse veel"+str(summa-raha))



    #8.2
# from datetime import *
# from random import *
# arve_nr = date.today()
# print(arve_nr)
# tsekk = "Arve: " + str(arve_nr) + "\nToode Hind Kogus Summa\n"
# summa = 0
# for toode in ["Pimm", "Leib","Komm"]:
#     hind = randint(50,150)/100
#     v = input("Toode:" + toode + " Hind: " + str(hind) + "\nKas tahd osta?").lower()
#     if v == "jah":
#         mitu = int(input("Mitu?"))
#         tsekk += toode + " " + str(hind) + " " + str(mitu) + " " + str(mitu + hind) + "\n"
#         summa += mitu * hind
# tsekk += "Kokku maksta: " + str(summa)
# print(tsekk)
# while True:
#     raha = float(input("Maksa "+str(summa)))
#     if raha == summa:
#         print("Tanan ostu eest!")
#         break
#     elif raha>summa:
#         print("Tana ostu eest! Tagasi " +str(raha-summa))
#         break
#     else:
#         summa -= raha
#         print("Makse veel"+str(summa))




    #10
arv1 = float(input("Sisetage esimene arv:"))
arv2 = float(input("Sisestage teine arv:"))
operatsioon = input("Valige kas (+, -, *, /): ")
if operatsioon == "+":
    vastus = arv1 + arv2
    print(vastus)
elif operatsioon == "-":
    vastus = arv1 - arv2
    print(vastus)
elif operatsioon == "*":
    vastus = arv1 * arv2
    print(vastus)
elif operatsioon == "/":
    vastus = arv1 / arv2
    print(vastus)
elif arv1 <=0:
    print("Ei saa jagada nulliga")
else:
   print("Viga. Kontrollige teie arv")


    #11
from datetime import *
from random import*
ta = datetime.today().year
print(ta)
sp = date(int(input("Sunniaasta")), int(input("Sunnikuu: ")), int(input("Sunnipaev:"))).year
if (ta-sp)%5 == 0:
    print("Juubel")
else:
    print("Tavaline sunnimpaev")



    #12
from math import *
import math
alghind = float(input("Sisestage alg hind:"))
if alghind <=10:
    soodus1 = alghind * 0.1
    lopphind = alghind - soodus1
    print("Teie soodus on 10%. Lõpp hind on:", round(lopphind, 2))
elif alghind <=20 and alghind >10:
    soodus2 = alghind * 0.2
    lopphind2 = alghind - soodus2
    print("Teie soodus on 20%. Lõpp hind on:", round(lopphind2, 2))



   #13
porand = input("Sisestage oma põrand (naine/mees):")
if porand == "mees":
   vanus= int(input("Sisestage oma vanus:"))
if porand == "naine":
    print("Vabandame, aga tee ei või regestreerida siin.")
if vanus == 16 and vanus <= 18:
    print("Tere tulemast meie meeskondis!")
else:
    print("Vabandame, aga tee ei või regestreerida siin.")


    #14

inimesed = int(input("Sisestage inimeste arv: "))
buss = int(input("Sisestage autobussi suurus: "))
bussiarv = inimesed / buss
print(round(bussiarv,1))
inimesed2 = inimesed / bussiarv
print(int(f"Teil on vaja (bussiarv))."))
print(int(f"Viimases bussis on (inimesed2) inimest."))

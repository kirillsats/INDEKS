#        # 1
# from string import *
# lause =input("Sisestage sõna või lause:").lower()
# lause_list = list(lause)
# vokaali = ["a", "e", "i", "o", "u", "ö", "ä", "õ", "ü" ]
# v=k=m=t=0
# konsonanti = ["b", "p", "d", "t", "g", "k", "s", "h", "f", "š", "z", "ž"]
# markid = punctuation
# for sümbool in lause_list:
#     if sümbool in vokaali:
#         v+=1
#     elif sümbool in konsonanti:
#         k+=1
#     elif sümbool in markid:
#         m+=1
#     elif sümbool==" ":
#         t+=1
# print("vokaali:", v)
# print("konsonanti:", k)
# print("Kirjuvahemärgid:", m)
# print("Tühikud:", t)
#
#
#
#       # 2
# nimed = []
# for i in range(5):
#     nimi = input("Sisesta nimed:")
#     nimed.append(nimi)
#
# print("Loetelu oli: ", nimed)
# nimed.sort()
# print( "Loetelu sorteeritud: ", nimed)
# for n in range(len(nimed)):
#     print(n+1,". ", nimed[n],sep="")
# print("Vimasena oli lisatud: ", nimi)
#
# uued_nimed = []
# for nimi in nimed:
#     if nimi not in uued_nimed:
#         uued_nimed.append(nimi)
# print(uued_nimed)
# #
# vanused = []
# for n in range(5):
#     vanus = int(input("Sisestage, kui vana sa oled: "))
#     vanused.append(vanus)
#
# maximum = max(vanused)
# minimum = min(vanused)
# print("Maksimum on: ",maximum)
# print("Minimum on: ",minimum)
# keskmine = (sum(vanused)) / (len(vanused))
# print("Keskmine on: ",keskmine)
# kokku = sum(vanused)
# print(kokku)
#  # print("Maksimum on:",maximum, "Minimum on:",minimum,"Keskmine on:",keskmine,"Kokki on: ",kokku)
# for i in range(5):
#         print(nimed[i],"on", vanused[i],"aastat vana")
#
# uued_nimed=list(set(nimed))
#
#
#
#
#     # 3
# from random import *
# arvud =[]
# N = int(input("Mitu rida joonistame"))
# S = input("Sisesta sümbol: ")
# for p in range(N):
#     arvud.append(randint(1,100))
# for p in range(N):
#     print(arvud[p]*S)
#
#
#
#
#     # 4
# ind =int(input("Valige millises maakonnas te elate: (1 – Tallinn,\n2 – Narva,\nNarva-Jõesuu,\n3 – Kohtla-Järve,\n4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa,\n5 – Tartu linn,\n6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa\n7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa,\n8 – Pärnumaa,\n9 – Läänemaa, Hiiumaa, Saaremaa,\n"))
#
# indeksid=["Tallinn","Narva, Narva-Jöesuu","Kohtla-Järve", "Ida-Virumaa,Lääne-Virumaa, Jögevamaa", "Tartu Linn", "Tartumaa, Pölvamaa, Virunaa,Valgamaa", "Viljandimaa, Järvamaa, Harjumaa,Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]
# while True:
#     while True:
#         try:
#             indeks = int(input("Sisestage viienumbriline indeks: "))
#             indeks_elemindide_arv = len(str(indeks))
#             if indeks_elemindide_arv == 5:
#                  print("5numbriline indeks")
#                  break
#             else:
#                 print("On vaja 5 numbriline indeks")
#         except:
#             print("Vale andmetüüp")
#     arv1 = indeks//10000
#     # print(arv1)
#     symbolid = list(str(indeks))
#     sym1 = symbolid[0]
#     # print(sym1)
#     if arv1 >0 or arv1<=3:
#         print("Istuge kodus")
#     if arv1 >3 or arv1 <=9:
#         print("Kanna maski ")
#
#
#     # 5
# arvud = input("Sisesta numbrid (ruumiga eraldatud): ").split()
# a, b = 0, len(arvud) - 1
# while a < b:
#     arvud[a], arvud[b] = arvud[b], arvud[a]
#     a, b = a + 1, b - 1
# print(arvud)
#
        # need 5 ülesanned tegin klassis.


             # 16
import random
kusimus = input("Sisestage teie küsimus(vastus peab olema Jah või Ei): ")
vastused = ["Jah", "kindlasti!", "Võib-olla!", "Ei!"]
juhuarv = random.randint(1, 4)
vastuss = vastused[juhuarv]
print(vastuss)



             # 12
import random

loend = [random.randint(1, 100) for i in range(10)]
# pp = loend+1
print("Nimekirja praegu", loend)
minimaalne = min(loend)
maksimaalne = max(loend)
indeks1 = loend.index(minimaalne)
indeks2 = loend.index(maksimaalne)
loend[0], loend[indeks1] = loend[indeks1], loend[0]
loend[-1], loend[indeks2] = loend[indeks2], loend[-1]
print("muudetud numbritega loend:", loend)




              # 6
loeng = [2, 7, 1, 8, 4, 10]
for i in loeng:
    if not loeng:
        print("Loeng on tühi.")
    else:
        maksimum = max(loeng)
        kasutu_arv = maksimum / len(loeng)
        loeng[loeng.index(maksimum)] = kasutu_arv
        print(f"tühi loeng: {loeng}")
        print(f"kasutu arv: {kasutu_arv}")
#



            #7
numbrid = [0, 1, 2, 3, -1, -2, -3]

sorterimine = sorted(numbrid)

print("Sorteeritud loend: ", sorterimine)






# Выведи на экран буквы имени в алфавитном порядке.(если буква встречается несколько раз, то повторять ее не надо)

            # 9
while True:
    nimi = input("Sisestage nimi: ")
    if nimi.isalpha():   #функцию подсмотрел в интернете
        break
    else:
        print("Sisestage ainult täht kirju: ")
print("Tere,",nimi.capitalize())
summ = sum(i.isalpha() for i in nimi)
print(summ)
vokaali = sum(i.isalpha() for i in nimi)
konsonanti = sum(i.isalpha() for i in nimi)
print("Summ on: " ,summ,",", "Vokaali arv on: ",vokaali,",", "Konsonanti arv on: ", konsonanti)
taht = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ü', 'õ', 'ä', 'ö', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
tahted = set()    #(создает пустое множество)
for i in nimi.lower():
    if i in taht:
        tahted.add(i)
mudustatud_tahted = sorted(tahted)
for i in mudustatud_tahted:
    print(i)



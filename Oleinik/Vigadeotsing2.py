print("*** Mängud numbritega ***")
print()
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage taisarv => "))))
        break
    except ValueError:
        print("See ei ole paaris arv")
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("See pole taisarv")
else:
    # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris-ja mitu paaritut numbrit")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
            b = b // 10

print("Numbrite arv:"+str(paaris))
print("Paaritu arv:"+str(paaritu))
print()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*Pöörake ümber sisestatud arv")
print()
b = 0
while a > 0:
    number = a % 10
    a = a // 10
    b = b * 10+ number
print("Pööratud arv "+str(b))
print()
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Uurime Syracuse hüpootesi")
print()
if c % 2 == 0:
    print("с - paarisarv. Jagame 2.")
else:
    print("с - paaritu arv. Koorutame 3-ga, liidame 1 и делим на 2.")
while c != 1:
    if c % 2 == 0:
        c == c / 2
    else:
        c == (3*c + 1)/2
    print("c, end=")
    print()
    print("Hüpotees on õige")
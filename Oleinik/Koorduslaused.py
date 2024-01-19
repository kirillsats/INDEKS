   #1
   #for
# r = 0
# for i in range(0, 15, 1):
#     arv=float(input("Sisesta {0}.arv".format(i+1)))
#     if arv ==  int(arv):
#         r += 1
# print("Taisarvude arv on "+str(r))

# r = 0
# i = 0
# while i<15:
#     i += 1
#     arv = float(input("Sisesta {0}.arv".format(i)))
#     if arv == int(arv):
#         r += 1
# print("Taisarvude arv on "+str(r))



     #2
# A = int(input("Sisestage arv A: "))
# r = 0
# for i in range(0, A + 1):
#     r += i
# print(f"Summ on {r}.")
r = 0
while True:
    A = int(input("Sisestage arv A: "))
    A += 1
    if A == int(A):
        r += 1
    if A <= 10:    break

print("Summ on " + str(r))




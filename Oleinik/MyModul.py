# def summa(arv1: int, arv2: int, arv3: int = 0) -> int:
#     """ Funktsioon tagastab kolme arvu summa
#         summa(arv1,arv2,arv3)
#
#     :param int arv1: Arv 1 sisestab kasutaja
#     :param int arv2: Arv 2 sisestab kasutaja
#     :param int arv3: Arv 3 vaikimisi arv 3 võrdub nulliga
#     :rtype: int
#     """
#     s = arv1 + arv2 + arv3
#     return s
#
#
# def tüüpkontroll(inp) -> str:
#     """ Funktsioon prindib väärtuse tüübi inp
#
#     :param inp: inp sisestab kasutaja
#     :rtype: str
#     """
#     try:
#         inp = int(inp)
#         return int
#     except:
#         try:
#             inp = float(inp)
#             return float
#         except:
#             try:
#                 inp = str(inp)
#                 return str
#             except:
#                 pass
#
#
# #
#
#         # 2
# def is_year_leap(year: int)->bool:
#     """Funktsioon otsustab kas aasta on liigasta või ei ole.
#     Tagstad True kui aasta on liigasta ja False kui aasta on tavaline aasta.
#
#     :param int year: Aasta sisestab kasutaja
#     :rtype: bool
#     """
#     if year%4==0 and year%100!=0:
#         return True
#     else:
#         return False
#
#
#
#         # 3
# from math import *
# def square(külg:float)->any:
#     """
#     Funktsioon ruudu küljel ja tagastab 3 vaartust: ruudu ümbermõt, ruudu pindala ja ruudu diagonaal
#     :param float külg:
#     :rtype: any
#     """
#     S=külg**2
#     p=külg*4
#     d=sqrt(2*külg**2)
#     return S,p,d
#
#         # 4
from math import *
def season(a:int)->str:
    """

    :param a:
    :return:
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a = int(input("Ainult 1-12! Sisestage number veel kord: "))
            except:
                print("Vigs andmetüübiga")

    if a== 12 or a==1 or a==2:
        s = "Talv"
    elif a>2 and a<6:
        s="Kevad"
    elif a in range(6,9,1):
        s = "Suvi"
    elif 9<=a<=11:
        s = "Sügis"
    return(s)



        # 5
def pank(a:int, years:int)->int:
    """Funktsioon, mis võtab deposiidi summa, kui vana see deposiit on ja tagastab deposiidi summa kasutaja kontole.
    param int i: deposiit sisestab kasutaja
    param years: aastased sisestab kasutaja
    rtupe: int
    """
    for year in range(years):
        a *= 1.1
    return a

            # 6

def is_prime(arv: int) -> bool:
    """Funktsioon, mis kontrollib, kas arv on lihtne või ei .
    Tagastab True, kui arv on lihtne
    Tagastab False, kui arv muidu
    param int arv: Sisestab kasutaja
    rtupe: bool
    """

    if arv == 1:
        return False
    for i in range(2, arv):
        if arv % i == 0:
            return False
    return True

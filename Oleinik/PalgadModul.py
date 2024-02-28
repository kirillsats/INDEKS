def inimeste_ja_palkade_liisamine(i:list,p:list,n=1)->any:
    """Funktisoon tagatab uendatud loendid, kus lisatud inimesi ja palka

    :param i:Inimeste järjend
    :param p:Palgate järjend
    :param n:Inimeste arv
    :rtype: List, list
    """
    if n>0:
        for j in range(n):
            nimi = input("Nimi: ").capitalize()
            palk = int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p


def andmed_veeerused(i: list, p: list):
    """Funktsioon kuvab ekraanile järjendite andmed veerudes

    :param i:  Inimeste järjend
    :param p: Palgate järjend
    """

    for j in range(len(i)):
        print(i[j],"-",p[j])

def andmete_kustutamine_nimi_jargi(i: list, p: list, n=1)->any:
    """Funktsioon kustutab andmeid ja tagastab loendid

    :param i: Inimeste järjend
    :param p: Palgate järjend
    :rtype: List, list
    """
    nimi = input("Keda kustutada ära(nimi): ")
    if nimi in i:
        for j in range(len(i)):
           if nimi in i:
               i.remove(nimi)
               p.pop(j)
        return i,p

def kellel_on_suurim_palk(i: list, p: list)->list:
    """Fumktisoon, mis näitab kellel on suurim palk

    :param i:Inimeste järjend
    :param p:Palgate järjend
    :rtype: List, list
    """
    nimed=[]
    maksimaalne = max(p)
    ind = -1
    for palk in p:
        if palk == maksimaalne:
            ind += 1
            nimi = i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_vaiksem_palk(i: list, p: list)->list:
    """Fumktisoon, mis näitab kellel on väiksem palk

    :param i:Inimeste järjend
    :param p:Palgate järjend
    :rtype: List, list
    """
    nimed=[]
    minimaalne = min(p)
    ind = -1
    for palk in p:
        if palk == minimaalne:
            ind += 1
            nimi = i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def sorteerimineA_Z(i: list, p: list):
    '''Funktsioon tagastab sorteerimised  palgad

    :param i: Inimeste järjend
    :param p: Palgate järjend
    :return:
    '''
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>m:
                p[m], p[n] = p[n], p[m]
                i[m], i[n] = i[n], i[m]
    return i,p

def sorteerimineZ_A(i: list, p: list):
    '''Funktsioon tagastab sorteerimised  palgad

    :param i: Inimeste järjend
    :param p: Palgate järjend
    :return:
    '''
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]<m:
                p[n], p[m] = p[m], p[n]
                i[n], i[m] = i[m], i[n]
    return i,p
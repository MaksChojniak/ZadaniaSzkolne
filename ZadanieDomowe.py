import math
import random


def v_szescian():
    a = float(input("podaj a: "))
    return a**3
    
def v_ostroslup_czworokatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return (a**2) * (1/3) * h

def  v_graniastoslup_trojkatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    H = float(input("podaj H: "))
    return (1/3) * a * h * H
    
    
    
def v_walec(r:float, h:float):
    return math.pi * (r ** 2) * h

def v_kuli(r:float):
    return (4/3) * math.pi * r**3

def v_stozek(r:float, h:float):
    return (1/3) * math.pi * r**2 * h
    
    
    
def v_piramidy(a:float, h:float):
    return a**2 * h / 3

def v_torus(r:float, R:float):
    return 2* math.pi ** 2 * r ** 2 * R

def v_kuli_odjac_v_torusa(r:float, R:float):
    return v_kuli(r) - v_torus(r, R)




def v_szescian_odjac_v_kuli(r:float):
    return v_szescian() - v_kuli(r)
    
def v_kuli_dodac_v_walca(r:float, h:float):
    print(v_kuli(r) + v_walec(r, h))
    
def v_szesciana_dodac_v_kuli(r:float):
    print(v_szescian() + v_kuli(r))
    
    
    
def v_szescian_dodac_v_stozek(r:float, h:float):
    print(v_szescian() + v_stozek(r, h))
    
def dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego():
    print ((2 * v_szescian()) + v_graniastoslup_trojkatny())
    
def v_walec_dodac_v_stozka_odjac_v_kuli():
    r = float(input("podaj r: "))
    h = float(input("podaj h: "))
    print(v_walec(r, h) + v_stozek(r, h) - v_kuli(r))



def v_piramidy_odjac_v_szescianu():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return v_piramidy(a, h) - v_szescian()
    
def  cztery_razy_v_stozka():
    r = float(input("podaj r: "))
    h = float(input("podaj h: "))
    return 4 * (v_stozek(r, h))
    
def v_walec_odjac_v_kuli(r:float, h:float):
    print(v_walec(r, h) - v_kuli(r))
    

def display_exercise():
    print("         KALKULATOR \n\n" +
          "1. v szeciana \n" +
          "2. v ostroslupa czworokatnego \n" +
          "3. v graniastoslupa trojkatnego" + 
          "4. v walca \n" +
          "5. v kuli \n" +
          "6. v stozka" + 
          "7. v piramidy \n" +
          "8. v torusa \n" +
          "9. v kuli odjac v torusa \n" + 
          "10. v szesciana odjac v kuli \n" +
          "11. v szesciana dodac v kuli" + 
          "12. v szescian_dodac_v_stozek \n" +
          "13. v kuli dodac v walca \n" +
          "14. v piramidy_odjac_v_szescianu \n" +
          "15. v cztery_razy_v_stozka \n" +
          "16. v walec_dodac_v_stozka_odjac_v_kuli \n" +
          "17. v walec_odjac_v_kuli \n" + 
          "18. v dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego \n \n" )

    while True:
        inp = int(input("wybierz co chcesz zrobic :  "))

        if inp == 1:
            print(v_szescian())
        elif inp == 2:
            print(v_ostroslup_czworokatny())
        elif inp == 3:
            print(v_graniastoslup_trojkatny())
        elif inp == 4:
             r = float(input("podaj r: "))
             h = float(input("podaj h: "))
             print(v_walec(r, h))
        elif inp == 5:
            r = float(input("podaj r: "))
            print(v_kuli(r))
        elif inp == 6:
            r = float(input("podaj r: "))
            h = float(input("podaj h: "))
            print(v_stozek(r, h))
        elif inp == 7:
            a = float(input("podaj a: "))
            h = float(input("podaj h: "))
            print(v_piramidy(a, h))
        elif inp == 8:
            r = float(input("podaj r: "))
            R = float(input("podaj R: "))
            print(v_torus(r, R))
        elif inp == 9:
            r = float(input("podaj r: "))
            R = float(input("podaj R: "))
            print(v_kuli_odjac_v_torusa(r, R))
        elif inp == 10:
            r = float(input("podaj r: "))
            print(v_szescian_odjac_v_kuli(r))
        elif inp == 11:
            r = float(input("podaj r: "))
            v_szesciana_dodac_v_kuli(r)
        elif inp == 12:
            r = float(input("podaj r: "))
            h = float(input("podaj h: "))
            v_szescian_dodac_v_stozek(r, h)
        elif inp == 13:
            r = float(input("podaj r: "))
            h = float(input("podaj h: "))
            v_kuli_dodac_v_walca(r, h)
        elif inp == 14:
            print(v_piramidy_odjac_v_szescianu())
        elif inp == 15:
            print(cztery_razy_v_stozka())
        elif inp == 16:
            v_walec_dodac_v_stozka_odjac_v_kuli()
        elif inp == 17:
            r = float(input("podaj r: "))
            h = float(input("podaj h: "))
            v_walec_odjac_v_kuli(r, h)
        elif inp == 18:
            dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego()
        else:
            print("podales zla liczbe sprobuj ponownie! ")

   


    # Control Flow


# zad 1.1
def zad11():
    inp = float(input("podaj r -> "))
    print(math.pi * r ** 2)

# zad 1.2
def zad12():
    a = random.randint(0, 1)
    for i in range(3):
        odp = int(input("liczba to -> "))
        if odp == a:
            print("wygrales")
            return 0
    print("przegrales")

# zad 1.3
def zad13():

    max_element = None
    while True:
        inp = input("")
        if inp == "stop":
            print("koniec najwiekszy element to " + str(max_element))
            return 0
        else:
            if max_element == None or max_element < float(inp):
                max_element = float(inp)

# zad 1.4
def zad14():
    a = float(input(""))
    b = float(input(""))
    c = float(input(""))
    

    if a > b and b > c:   # a b c
        zad14_2(a,b,c)
    if a > b and b < c:   # a c b
        zad14_2(a,c,b)
    if b > c and c > a:   # b c a
        zad14_2(b,c,a)
    if b > c and c < a:   # b a c
        zad14_2(b,a,c)
    if c > a and a > b:   # c a b
        zad14_2(c,a,b)
    if c > a and a < b:   # c b a
        zad14_2(c,b,a)

def zad14_2(a:float, b:float, c:float):
    if a**2 == b**2 + c**2:
        print("da sic zrobic")
    else:
        print("nie da sie zrobic")


# zad 1.5
def zad15():
    odcinki = []
    inp = int(input("podaj odcinek (dlugodc min 4) -> "))
    for i in range(2):
        r = random.randint(1, inp-2)
        inp -= r
        odcinki.append(r)
    odcinki.append(inp)
    print(odcinki)
    

# zad 1.6
def zad16():
    n = int(input(""))
    zad16_2(n)

def zad16_2(n:int):
    liczby = []

    num = 1
    ile = 0

    while len(liczby) < n:

        for i in range(1, num + 1):
            if num % i == 0:
                ile += 1
        print("ile dzielnikow -> " + str(ile) + "dla liczby -> " + str(num))
        if ile == 2:
            liczby.append(num)
        ile = 0
        num += 1
    
    print(liczby)
           




    # Listy

def zad21():
    tab = [2, 21, 7, 13, 17, 14, 28, 33]
    tab2 = []

    for i in range(len(tab)):
        if tab[i] % 7 == 0:
            tab2.append(tab[i])

    print(tab2)

def zad22(a:float):
    tab = [1, 2, 5, 7, 8, 2, 12, 0]
    suma = 0

    for i in range(len(tab)):
        if tab[i] % a == 0:
            suma += tab[i]

    print(suma)


def zad23(a:float):
    tab = [1, 12, 1, 15, 19, 12, 1] 
    ile = 0
    for i in range(len(tab)):
        if tab[i] == a:
            ile += 1
    print(ile)


def zad24():
    tab = [-10, 1, 2, -5, -10, -10, -1, 10]
    min_v = tab[0]
    min_i = []

    for i in range(len(tab)):
        if tab[i] < min_v:
            min_v = tab[i]

    for i in range(len(tab)):
        if tab[i] == min_v:
            min_i.append(i)

    print(str(min_v) + "   " +str(min_i))


def zad25():
    tab = [1, 10, 5, 2, 11, -10, 8]
    suma_har = 0
    for i in range(len(tab)):
        suma_har += 1/ tab[i]

    print(suma_har / len(tab))

def zad26():
    tab = [1, 2, 4, 9, 16, 10, 16]
    indexy = []
    liczby = []

    for i in range(len(tab)):
        if math.sqrt(tab[i]) % 1 == 0:
            indexy.append(i)
    
    for i in range(len(indexy)):
        liczby.append(tab[indexy[i]])

    print(liczby)






    # Funkcje


def zad31():
    tab = [1, 5 ,3, 5, 6, 8 ,9, 8, 54, 2,1, 8, 2,56, 12, 134, 1, -100, 1, 12]
    suma = 0

    for i in range(len(tab)):
        suma += tab[i]

    print( suma / len(tab) )


def zad32():
    a = [1, -2, 10 , -100, -100, -100]

    min_index = []
    min_value = a[0]
    i = 0
    while i < len(a):
        if min_value > a[i]:
            min_value = a[i]
            min_index.clear()
            min_index.append(i)
        elif min_value == a[i]:
            min_index.append(i)
        i += 1
    print(min_index)


def zad33(n:int, k:float):
    tab = []
    for i in range(n):
        tab.append(k ** (2 + i))
    print(tab)


def zad34():
    b = False
    B = True

    if b == B:
        return 1
    else:
        return 0

    print(xx(true, false))


def zad35(n:int):
    ciag = [1,2,3,4,5,6,7,8,9,10,11]
    tab = []
    for i in range(n):
        if i >= len(ciag):
            tab.append(ciag[i-len(ciag)])
        else:
            tab.append(ciag[i])
    print(tab)



def zad36_2(r:float):
    return math.pi * r ** 2

def zad36():
    r1 = float(input(" "))
    r2 = float(input(" "))
    print( zad36_2(r1) - zad36_2(r2) )
    




    # Funkcje for/while

def zad41():
    tab = [10, 1, -10, 1, 11, 10, -15, 2]
    max_v = tab[0]

    for i in range(len(tab)):
        if tab[0] > max_v:
            max_v = tab[i]
    print(max_v)

def zad42(n:int):
    tab = []
    for i in range(n):
        a = random.randint(1, 100)
        if a % 5 == 0:
            tab.append(a)

    print(tab)

def zad43(m:int, k:int, c:int):
    tab = []
    for i in range(m):
        if k < c:
            tab.append(random.randint(k, c))
        else:
            tab.append(random.randint(c, k))

    print(tab)

def zad44(n:int):
    tab = []
    
    i = 1
    ile_r = 0

    while len(tab) < n:
        for j in range(1, i + 1):
            if i % j == 0:
                ile_r += 1
        print(str(i) + "   " + str(ile_r))
        if ile_r == 2:
            tab.append(i)
        i +=1
        ile_r = 0
    print(tab)

def zad45(n:int):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 100))
    print(zad45_2(tab))

def zad45_2(tab):
    tab1 = []
    tab2 = []

    for i in range(len(tab)):
        if tab[i] % 2 == 0:
            tab1.append(tab[i])
        else:
            tab2.append(tab[i])
    return tab1, tab2


def zad46(a, A, arg):
    ile_r_a = 0
    ile_r_A = 0

    tab = []
    tab = [i for i in arg]
    for i in range(len(tab)):
        if tab[i] == a:
            ile_r_a += 1
        elif tab[i] == A:
            ile_r_A += 1
    
    print(str(ile_r_a) + "   " + str(ile_r_A) )


    # 5 zadan Rozszerzenie z githuba

# zad 5.1
def zad51(tablica):
    suma_sr_ar = []
    suma_sr_har = []

    for i in range(len(tablica)):
        suma_sr_ar.append(0)
        suma_sr_har.append(0)

        for j in range(len(tablica[i])):
            suma_sr_ar[i] += tablica[i][j]
            suma_sr_har[i] += 1 / tablica[i][j]

        suma_sr_ar[i] = suma_sr_ar[i] / len(tablica[i])
        suma_sr_har[i] = suma_sr_har[i] / len(tablica[i])

    print("srednia arytmetyczna --> " + str(suma_sr_ar))
    print("srednia harmoniczna --> " + str(suma_sr_har))


# zad 5.2

def zad52(tablica):
    suma_sr_ar = 0

    for i in range(len(tablica)):
        suma_sr_ar = 0

        for j in range(len(tablica[i])):
            suma_sr_ar += tablica[i][j]

        suma_sr_ar = suma_sr_ar / len(tablica[i])
        print("srednia arytmetyczna --> " + str(suma_sr_ar) + " o indexie --> " + str(i))

# zad 5.3

def zad53(tablica):
    my_max = 0

    for i in range(len(tablica)):
        if tablica[i] > my_max:
            my_max = tablica[i]

    print(my_max)

# zad 5.4

def zad54_1(tablica, k:float):

    n_tablica = []

    for i in range(len(tablica)):
        if tablica[i] % k == 0:
            n_tablica.append(tablica[i])

    return n_tablica

def zad54_2(tablica):

    for i in range(len(tablica)):
        print(str(tablica[i]) + "\t")


# zad 5.5
import random

def zad55_1(tablica):
    tab = []

    for i in range(len(tablica)):
        tab.append([])
        
        for j in range(len(tablica[i])):
            tab[i].append(random.randint(1, 100))

    return tab

def zad5_2(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            print(str(tablica[i][j]) + "\t")



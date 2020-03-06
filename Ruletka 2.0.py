import random
import sys
import time
print('Witamy w Ruletce 2.0. Jeżeli grałeś w poprzednią wersję to odrazu zauważysz poprawę w jej funkcjonowaniu. Jeśli nie, to i tak mamy nadzieję, że docenisz tą grę.')
time.sleep(5)
print('Zasady gry są proste. Będziesz miał możliwość zagrania w ruletkę 3 razy. Za każdym razem będziesz musiał podać stawkę jaką chcesz zagrać oraz wybrać kolor na który postawisz podaną stawkę.')
time.sleep(6)
print('W ramach promocji nowej wersji gry proponujemy Ci grę kwotą tysiąca złotych, która dostajesz od nas w prezencie. Czy przyjmujesz proponowany podarunek?')
time.sleep(1)
global a
a=input()
while a: 
    if a!='tak' and a!='Tak' and a!='nie' and a!='Nie':
        print('Podana odpowiedź nie jest poprawna. Musisz odpowiedzieć Tak lub Nie.')
        print('Spróbuj jeszcze raz.')
        a=input()
    if a=='tak' or a=='Tak':
        print('Twoja odpowiedź brzmi Tak.')
        time.sleep(1)
        print('Cieszymy się, że zachęciliśmy Cię do skorzystania z proponowanego bonusu.')
        time.sleep(2)
        print('W związku z tym na ten moment posiadasz 1000 złotych.')
        time.sleep(2)
        print('W takim razie rozpoczynamy grę w wirtualną ruletkę.Życzymy Ci powodzenia!')
        break
    if a=='nie' or a=='Nie':
        print('Twoja odpowiedź brzmi Nie.')
        time.sleep(1)
        print('Mamy nadzieję, że następnym razem zachęcimy Cię do skorzystania z naszych bonusów.')
        time.sleep(2)
        print('W takim razie rozpoczynamy grę w wirtualną ruletkę.Życzymy Ci powodzenia!')
        break
time.sleep(2)
print('Rozpoczynamy pierwszą rundę gry. Prosimy o podanie stawki.')
print('Wysokość stawki:',end='')
global b
b=input()
while b:
    if int(b)<=0:
        print('Podana przez Ciebie stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę:', end='')
        b=input()
    if  b==str():
        print('Podana stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę:', end='')
        b=input()
    if int(b)>0:
        print('Podana przez Ciebie stawka wynosi ' + str(b) + ' złotych.')
        break
def qw():  #wybrany kolor-czerwony
    v=random.randint(1,5)
    if v==1:
        qa()
    elif v==2:
        qz()
    elif v==3:
        qx()
    elif v==4:
        qc()
    elif v==5:
        qv()
def qa():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czerwona 25!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qz():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czerwona 19!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qx():
    print('Niestety. Wypadła czarna 31.')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    global y
    if str(a)!='tak' and str(a)!='Tak':
        y==0
        print('Obecnie na koncie masz 0 złotych.')
    if str(a)=='tak' or str(a)=='Tak':
        y=1000-int(b)
        print('Na koncie pozostało Ci ' + str(y) + ' złotych.')
def qc():
    print('Niestety. Wypadło 0.')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    global y
    if str(a)!='tak' and str(a)!='Tak':
        y==0
        print('Obecnie na koncie masz 0 złotych.')
    if str(a)=='tak' or str(a)=='Tak':
        y=1000-int(b)
        print('Na koncie pozostało Ci ' + str(y) + ' złotych.')
def qv():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czerwona 1!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qe():    #wybrany kolor-czarny
    v=random.randint(1,5)
    if v==1:
        qb()
    elif v==2:
        qn()
    elif v==3:
        qm()
    elif v==4:
        qf()
    elif v==5:
        qg()
def qb():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czarna 15!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qn():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czarna 10!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qm():
    global y
    y=int(b)*2
    print('Gratulacje! Wypadła czarna 13!')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(y) + ' złotych.')
def qf():
    print('Niestety. Wypadła czerwona 5.')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    global y
    if str(a)!='tak' and str(a)!='Tak':
        y==0
        print('Obecnie na koncie masz 0 złotych.')
    if str(a)=='tak' or str(a)=='Tak':
        y=1000-int(b)
        print('Na koncie pozostało Ci ' + str(y) + ' złotych.')
def qg():
    print('Niestety. Wypadła czerwona 3.')
    time.sleep(1)
    print('Postawiłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(b) + ' złotych.')
    time.sleep(2)
    global y
    if str(a)!='tak' and str(a)!='Tak':
        y==0
        print('Obecnie na koncie masz 0 złotych.')
    if str(a)=='tak' or str(a)=='Tak':
        y=1000-int(b)
        print('Na koncie pozostało Ci ' + str(y) + ' złotych.')
time.sleep(2)
print()
print('Teraz musisz zdecydować na który kolor postanawiasz postawić:czerwony czy czarny.')
time.sleep(2)
print()
print('Podaj wybrany kolor:',end='') 
global c
c=input()
while c:
    if c=='Czerwony' or c=='czerwony':
        print('Wybrałeś kolor ' + str(c)+ '.')
        qw()
        break
    if c=='Czarny' or c=='czarny':
        print('Wybrałeś kolor ' + str(c) + '.')
        qe()
        break
    if c!='Czerwony' and c!='czerwony' and c!='Czarny' and c!='czarny':
        print('Podany przez Ciebie kolor nie jest poprawny.Prosimy spróbować jeszcze raz.')
        time.sleep(1)
        print('Podaj wybrany kolor:', end='')
        c=input()
time.sleep(1)
print('Czas na drugie kręcenie ruletką.')
time.sleep(1)
print('Prosimy podać stawkę:', end='')
time.sleep(1)
global u
u=input()
while u:
    if int(u)<=0:
        print('Podana przez Ciebie stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę:', end='')
        u=input()
    if u==str():
        print('Podana stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę:', end='')
        u=input()
    if int(u)>int(y):
        print('Podana stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę:', end='')
        u=input()
    if int(u)>0:
        print('Podana przez Ciebie stawka wynosi ' + str(u) + ' złotych.')
        break
def qr():  #wybrany kolor-czerwony,drugie kręcenie
    e=random.randint(1,5)
    if e==1:
        qh()
    elif e==2:
        qj()
    elif e==3:
        qk()
    elif e==4:
        ql()
    elif e==5:
        qq()
def qh():
    global p
    p=int(u)*2+int(y)
    print('Gratulacje! Wypadła czerwona 16!')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(p) + ' złotych.')
def qj():
    global p
    p=int(u)*2+int(y)
    print('Gratulacje! Wypadła czerwona 18!')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(p) + ' złotych.')
def qk():
    global p
    print('Niestety. Wypadła czarna 8.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(y)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
def ql():
    global p
    print('Niestety. Wypadła czarna 10.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(y)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
def qq():
    global p
    print('Niestety. Wypadła czarna 8.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(y)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
def qt():  #wybrany kolor-czarny,drugie kręcenie
    e=random.randint(1,5)
    if e==1:
        qqa()
    elif e==2:
        qqz()
    elif e==3:
        qqx()
    elif e==4:
        qqc()
    elif e==5:
        qqv()
def qqa():
    global p
    p=int(u)*2+int(y)
    print('Gratulacje! Wypadła czarna 26!')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(p) + ' złotych.')
def qqz():
    global p
    p=int(u)*2+int(y)
    print('Gratulacje! Wypadła czarna 35!')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(p) + ' złotych.')
def qqx():
    print('Niestety. Wypadła czerwona 36.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    global p
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(y)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
def qqc():
    global p
    print('Niestety. Wypadła czerwona 19.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(u)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
def qqv():
    global p
    print('Niestety. Wypadła czerwona 21.')
    time.sleep(1)
    print('Postawiłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(u) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(y)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(y)>0:
            p=int(d)-int(u)
            print('Obecnie masz na koncie ' + str(p) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        p=int(y)-int(u)
        print('Na koncie pozostało Ci ' + str(p) + ' złotych.')
time.sleep(2)
print()
print('Teraz musisz zdecydować na który kolor postanawiasz postawić:czerwony czy czarny.')
time.sleep(2)
print()
print('Podaj wybrany kolor:',end='')
global la
la=input()
while la:
    if la=='Czerwony' or la=='czerwony':
        print('Wybrałeś kolor ' + str(la)+ '.')
        qr()
        break
    if la=='Czarny' or la=='czarny':
        print('Wybrałeś kolor ' + str(la) + '.')
        qt()
        break
    if la!='Czerwony' and la!='czerwony' and la!='Czarny' and la!='czarny':
        print('Podany przez Ciebie kolor nie jest poprawny.Prosimy spróbować jeszcze raz.')
        time.sleep(1)
        print('Podaj wybrany kolor:', end='')
        la=input()
time.sleep(1)
print('Czas na trzecie kręcenie ruletką.')
time.sleep(1)
print('Prosimy podać stawkę: ', end='')
st=input()
while st:
    if int(st)<=0:
        print('Podana przez Ciebie stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę: ', end='')
        st=input() 
    if st==str():
        print('Podana stawka nie jest poprawna.Prosimy spróbować jeszcze raz.')
        print('Podaj poprawną stawkę: ', end='')
        st=input()
    if int(st)>0:
        print('Podana przez ciebie stawka wynosi ' + str(st) + ' złotych.')
        break   
def qy():        #trzecie kręcenie, wybrany kolor-czerwony
    ve=random.randint(1,5)
    if ve==1:
        qqb()
    elif ve==2:
        qqn()
    elif ve==3:
        qqm()
    elif ve==4:
        qqf()
    elif ve==5:
        qqg()
def qqb():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czerwona 27!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qqn():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czerwona 1!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qqm():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czerwona 16!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qqf():
    global d
    print('NIestey. Wypadła czarna 6.')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(p)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(p)>0:
            d=int(p)-int(st)
            print('Obecnie masz na koncie ' + str(d) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        d=int(p)-int(st)
        print('Na koncie pozostało Ci ' + str(d) + ' złotych.')
def qqg():
    global d
    print('NIestey. Wypadła czarna 8.')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(p)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(p)>0:
            d=int(p)-int(st)
            print('Obecnie masz na koncie ' + str(d) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        d=int(p)-int(st)
        print('Na koncie pozostało Ci ' + str(d) + ' złotych.')
def qu():                   #kręcenie trzecie, wybrany kolor-czarny
    et=random.randint(1,5)
    if et==1:
        qqh()
    elif et==2:
        qqj()
    elif et==3:
        qqk()
    elif et==4:
        qql()
    elif et==5:
        qqp()
def qqh():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czarna 34!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qqj():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czarna 4!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qqk():
    global d
    d=int(st)*2+int(p)
    print('Gratulacje! Wypadła czarna 17!')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Zyskałeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Obecnie na koncie masz ' + str(d) + ' złotych.')
def qql():
    global d
    print('Niestety. Wypadła czerwona 12.')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(p)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(p)>0:
            d=int(p)-int(st)
            print('Obecnie masz na koncie ' + str(d) + ' złotych')
    if str(a)=='tak' or str(a)=='Tak':
        d=int(p)-int(st)
        print('Na koncie pozostało Ci ' + str(d) + ' złotych.')
def qqp():
    global d
    print('Niestety. Wypadła czerwona 7.')
    time.sleep(1)
    print('Postawiłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    print('Straciłeś ' + str(st) + ' złotych.')
    time.sleep(2)
    if str(a)!='tak' and str(a)!='Tak':
        if int(p)<=0:
            print('Obecnie masz na koncie 0 złotych.')
        if int(p)>0:
            d=int(p)-int(st)
            print('Obecnie masz na koncie ' + str(d) + ' złotych.')
    if str(a)=='tak' or str(a)=='Tak':
        d=int(p)-int(st)
        print('Na koncie pozostało Ci ' + str(d) + ' złotych.')
time.sleep(2)
print()
print('Teraz musisz zdecydować na który kolor postanawiasz postawić:czerwony czy czarny.')
time.sleep(2)
print()
print('Podaj wybrany kolor:',end='')
global le
le=input()
while le:
    if le=='Czerwony' or le=='czerwony':
        print('Wybrałeś kolor ' + str(le)+ '.')
        qy()
        break
    if le=='Czarny' or le=='czarny':
        print('Wybrałeś kolor ' + str(le) + '.')
        qu()
        break
    if le!='Czerwony' and le!='czerwony' and le!='Czarny' and le!='czarny':
        print('Podany przez Ciebie kolor nie jest poprawny.Prosimy spróbować jeszcze raz.')
        time.sleep(1)
        print('Podaj wybrany kolor:', end='')
        le=input()
time.sleep(2)
print('Dotarłeś do końca naszej gry.')
time.sleep(1)
if str(a)!='tak' and str(a)!='Tak':
    if int(d)<=0:
        print('Po zakręceniu trzy razy ruletką na twoim koncie znajduje się 0 złotych.')
        time.sleep(2)
        print('Jest nam przykro, że nie udało Ci się pomnożyć pieniędzy. Mamy nadzieje, że jeszcze kiedyś wrócisz do nas.')
        time.sleep(3)
    if int(d)>0:
        print('Po zakręceniu trzy razy ruletką na twoim koncie znajduje się ' + str(d) + ' złotych.')
        time.sleep(2)
        print('Cieszymy się, że udało Ci się pomnożyć twoje pieniądze.')
if str(a)=='tak' or str(a)=='Tak':
    if int(d)>1000:
        i=int(d)-1000
        print('Gratulacje. Zyskałeś ' + str(i) + ' złotych.')
    if int(d)==1000:
        print('Niestety. Nie udało Ci się pomnożyć przyznanego bonusu.Zachęcamy do ponownej gry.')
    if int(d)<1000 and int(d)>0:
        i=1000-int(d)
        print('Niestety. Straciłeś ' + str(i) + ' złotych z przyznanego Ci bonusu.')
    if int(d)<=0:
        print('Niestety straciłeś w całości bonus, który został Ci przez nas przyznany.')
print()
time.sleep(2)
print('Ciekawe dane statystyczne.')
time.sleep(2)
if int(b)>int(st) and int(b)>int(u):
    print('Twoją najwyższą stawką było ' + str(b) + ' złotych.')
if int(u)>int(b) and int(u)>int(st):
    print('Twoją najwyższą stawką było ' + str(u) + ' złotych.')
if int(st)>int(b) and int(st)>int(u):
    print('Twoją najwyższą stawką było ' + str(st) + ' złotych.')
time.sleep(2)
if (str(c)=='czerwony' or str(c)=='Czerwony') and (str(la)=='czerwony' or str(la)=='Czerwony'):
    print('Częściej stawiałeś na kolor czerwony niż na czarny.')
if (str(c)=='czarny' or str(c)=='Czarny') and (str(la)=='czarny' or str(la)=='Czarny'):
    print('Częściej stawiałeś na kolor czarny niż czerwony.')
if (str(c)=='czerwony' or str(c)=='Czerwony') and (str(le)=='czerwony' or str(le)=='Czerwony'):
        print('Częściej stawiałeś na kolor czerwony niż na czarny.')
if (str(c)=='czarny' or str(c)=='Czarny') and (str(le)=='czarny' or str(le)=='Czarny'):
    print('Częściej stawiałeś na kolor czarny niż czerwony.')
if (str(le)=='czerwony' or str(le)=='Czerwony') and (str(la)=='czerwony' or str(la)=='Czerwony'):
    print('Częściej stawiałeś na kolor czerwony niż na czarny.')
if (str(le)=='czarny' or str(le)=='Czarny') and (str(la)=='czarny' or str(la)=='Czarny'):
    print('Częściej stawiałeś na kolor czarny niż czerwony.')
time.sleep(2)
print()
print('Jeśli spodobała Ci się gra lub chciałbyś spróbować sie odkuć, bo Ci się nie powiodło to zapraszamy do ponownego zagrania.')
time.sleep(3)
print()
print('Będziemy wdzięczni jeśli będziesz chciał wyrazić swoją opinię na temat Ruletki 2.0.')
print()
time.sleep(2)
print('Czy zgadzasz się na udział w krótkiej ankiecie?')
print()
time.sleep(2)
print('Prosimy o odpowiedź Tak lub Nie.')
vmn=input()
if str(vmn)=='Tak':
    print
    print('Czy podoba Ci się system gry?')
    time.sleep(2)
    print('Prosimy o odpowiedź Tak lub Nie')
    vb=input()
    while str(vb)!='Tak' or str(vb)!='Nie':
        print('Podana odpowiedź nie jest poprawna.Prosimy spróbować jeszcze raz.')
        time.sleep(1)
        print('Twoja odpowiedź ',end='')
        vb=input
    print()
    time.sleep(1)
    print('Czy polecisz Ruletkę 2.0 swoim znajomym?')
    print()
    time.sleep(2)
    print('Prosimy o odpowiedź Tak lub Nie.')
    time.sleep(2)
    vio=input()
    while str(vio)!='Tak' or str(vio)!='Nie':
        print('Podana odpowiedź nie jest poprawna.Prosimy spróbować jeszcze raz.')
        time.sleep(1)
        print('Twoja odpowiedź ',end='')
        vio=input
    print()
    print('Dziękujemy za udział w ankiecie.Doceniamy twoją chęć jej wypełnienia.Podane przez Ciebie odpwoeidzi wpłyną na poprawę wizualna oraz funkcjonowanie gry.')
    time.sleep(4)
if str(vmn)=='Nie':
    print('Rozumiemu, że się nie zgadzasz.Rozumiemy twoją decyzje.W takim razie dziękujemy za grę w Ruletke 2.0.')
while str(vmn)!='Tak' and str(vmn)!='Nie':
    print('Podana odpowiedź nie jest poprawna.Prosimy spróbować jeszcze raz.')
    vmn=input()
print()
print('Na sam koniec mamy prośbę....')
time.sleep(3)
print()
print('Nie zostań hazardzista!!')

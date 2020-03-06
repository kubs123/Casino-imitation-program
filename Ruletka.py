print('Witaj w wirtualnej grze w ruletke. Dostajesz od nas tysiąc złotych, które możesz pomnożyć lub stracić. Masz trzy zakręcenia ruletką. Powodzenia.')
print()
print('Czas na pierwsze kręcenie. Podaj stawkę:', end='')
global b
b=1000
a=input()
while int(a)<=0 or int(a)>1000:
    print('Podana wartoścć jest niepoprawna. Proszę spróbować jeszcze raz')
    print()
    print('Podaj poprawną stawkę:', end='')
    a=input()
import random
def ab(a):
    global b
    b=int(b)-int(a)
    a=int(a)*1.2
    global c
    c=int(b)+int(a)
    print('Gratuluje, wygrałeś ' + str(a) + ' złotych. Obecnie masz ' + str(c) + ' złotych.')
def ac(a):
    global b
    a=int(a)
    global c
    c=int(b)-int(a)
    print('Niestety przegrałeś. Obecnie masz ' + str(c) + ' złotych.')
def ad(a):
    global b
    a=int(a)
    global c
    c=int(b)-int(a)
    print('Niestety przegrałeś. Obecnie masz ' + str(c) + ' złotych.')
def ae(a):
    global b
    b=int(b)-int(a)
    a=int(a)*1.5
    global c
    c=int(b)+int(a)
    print('Gratulacje, wygrałeś ' + str(a) + ' złotych. Obecnie masz ' + str(c) + ' złotych.')
v = random.randint(1,4)
if v == 1:
    ab(a)
elif v == 2:
    ac(a)
elif v == 3:
    ad(a)
elif v == 4:
    ae(a)
import sys
global c
while c<=0:
    print('Nie posiadasz wystarczających funduszy do dalszej gry. Koniec gry')
    sys.exit(0)
print('Czas na drugie kręcenie. Podaj stawkę:', end='')
d=input()
while c<int(d):
    print('Podana wartość nie jest poprawna. Proszę spróbować jeszcze raz.')
    print('Podaj poprawną stawkę: ', end='')
    d=input()
c=int(c)-int(d)
import random
def af(d):
    d=int(d)*1.5
    global e
    e=int(c)+int(d)
    print('Gratulacje, wygrałeś ' + str(d) + ' złotych. Obecnie masz ' + str(e) + ' złotych.')
def ag(d):
    d=int(d)
    global e
    e=int(c)-int(d)
    print('Niestety przegrałeś. Obecnie masz ' + str(e) + ' złotych.')
def ah(d):
    d=int(d)
    global e
    e=int(c)-int(d)
    print('Niestety przegrałeś. Obecnie masz ' + str(e) + ' złotych.')
def ai(d):
    d=int(d)*3.2
    global e
    e=int(c)+int(d)
    print('Gratulacje, wygrałeś ' + str(d) + ' złotych. Obecnie masz ' + str(e)+ " złotych.")
v = random.randint(1,4)
if v == 1:
    af(d)
elif v == 2:
    af(d)
elif v == 3:
    af(d)
elif v == 4:
    af(d)
global e
while e<=0:
    print('Nie posiadasz wystarczających funduszy do dalszej gry. Koniec gry')
    sys.exit(0)
print('Czas na ostatnie kręcenie. Podaj stawkę:', end='')
y=input()
while e<int(y):
    print('Podana wartość nie jest poprawna. Proszę spróbować jeszcze raz.')
    print('Podaj poprawną stawkę: ', end='')
    y=input()
e=int(e)-int(y)
import random
def aj(y):
    y=int(y)*2
    global p
    p=int(e)+int(y)
    print('Gratulacje, wygrałeś ' + str(y) +  ' złotych. Obecnie masz ' + str(p) + ' złotych.')
def ak(y):
    y=int(y)
    global p
    p=int(e)-int(y)
    if p>=0:
        print('Niestety przegrałeś. Obecnie masz ' + str(p) + ' złotych.')
    else:
        print('Niestety straciłeś wszystkie swoje pieniądze.')
def al(y):
    y=int(y)
    global p
    p=int(e)-int(y)
    if p>=0:
        print('Niestety przegrałeś. Obecnie masz ' + str(p) + ' złotych.')
    else:
        print('Niestety straciłeś wszystkie swoje pieniądze.')
def am(y):
    y=int(y)*4
    global p
    p=int(e)+int(y)
    print('Gratulacje, wygrałeś ' + str(y) + ' złotych. Obecnie masz ' + str(p) + ' złotych.')
v = random.randint(1,4)
if v == 1:
    aj(y)
elif v == 2:
    ak(y)
elif v == 3:
    al(y)
elif v == 4:
    am(y)
global p
b==1000
if int(b)>int(p):
    print('Niestety ale straciłeś ' + str(b) + ' złotych oraz wszystkie zarobione pieniądze.')
if int(b)<int(p):
    r=int(p)-int(b)
    print('Gratulacje, zyskałeś ' + str(r) + ' złotych')
print('Dziękujemy za udział w grze. Zapraszamy ponownie po jeszcze więcej emocji.')

#funkcja łącząca tekst
def zlacz_teksty(lista):
    return " ".join(lista)

lista = ["A", "B", "C"]
print(zlacz_teksty(lista))

t1 = "A"
t2 = "B"
t3 = "C"

#funkcja z *args
def zlacz_teksty(*args):                            #args to nieokreślona liczba argumentów (to jest tupla), kwargs to słownik
    text = "\n".join(args)
    return text
print(zlacz_teksty(t1,t2))                          #A
                                                    #B

print(zlacz_teksty(t1,t2, "cos"))                   #A
                                                    #B
                                                    #cos

#funkcja z *args i **kwargs
def zlacz_teksty(*args, **kwargs):      #args to nieokreślona liczba argumentów (to jest tupla), kwargs to słownik
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace(k, str(v))              #w text zamień ze k (k to jest klucz) na wartość v ze słownika - kwargs to słownik
    return text

slownik = dict(x=1, y=2)
print(slownik)                                      #{'x': 1, 'y': 2}

print(zlacz_teksty(t1, t2, t3, A="X", y=15, z=25))    # X B C (w t1 pojawiło się X zamiast A)
print(zlacz_teksty(t1, t3))                         #A C
print("-"*40)
print(zlacz_teksty(t1, "xxx", x="na"))              #A, jeśli w tekście jest x to zastąp x wartością "na"       #A, nanana
print(zlacz_teksty(t1, "xxx", z="na"))              #A, jeśli w tekście jest x to zastąp x wartością "na"       #A, xxx
print(zlacz_teksty(t1, "y", y="na"))                #A, jeśli w tekście jest y to zastąp y wartością "na"       A, na

print("-"*40)


#Zaimplementuj funkcję formatującą podane napisy.
#Przykład użycia:
#>>> formatuj('koszt $cena PLN','kwota $cena brutto',cena=10 )
#'koszt 10 PLN\nkwota 10 brutto'

def form(*a):                                       #możemy podać dowolną ilość argumentów
    x = "\n".join(a)
    return x

print(form("cos", "jest", "nie", "tak"))
#cos
#jest
#nie
#tak

t = "jakis tekst"
print(t.replace("j", "-"))                                          #-akis tekst

def formatuj(*teksty, **znaczniki):
    text = "\n".join(teksty)                                        #każdy *teksty jest połączony z nową linią
    for znacznik, wartosc in znaczniki.items():                     #znacznikiem domyślnie jest cena, wartośćią domyślnie jest 10
        text = text.replace("$"+znacznik, str(wartosc))             #w tekście $cena zastąp wartością 10 (tylko jeśli jest słowo cena w kwargs)
    return text

print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10))
print()
print(formatuj('koszt $cena PLN', 'kwota $cena brutto'))
print()
print(formatuj('koszt $cena PLN', 'kwota $cena brutto', podatek=15))

def test_formatuj():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto') == 'koszt $cena PLN\nkwota $cena brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', podatek=15) == 'koszt $cena PLN\nkwota $cena brutto'
    assert formatuj('koszt $cena PLN', 'kwota podatku $podatek', podatek=15) == 'koszt $cena PLN\nkwota podatku 15'
    assert formatuj('koszt $cena PLN', podatek=15) == 'koszt $cena PLN'

#*args są bez równa się
#kwargs są tam gdzie cena=10

def foo(a, *args, x=1, **kwargs):
    print("Argument a: ", a)
    print("*args", args)
    print("x", x)
    print("**kwargs", kwargs)
    print("-"*40)

foo(10)
#wynik:
#Argument a:  10
#*args ()
#x 1
#**kwargs {}

foo(12, 14, 23, "A",  x=20, y=30, z=10)
#wynik:
#Argument a:  12                                #przyporządkowanie 12 do argumentu a
#*args (14, 23, 'A')                            #przyporządkowanie 14, 23, A do dowolnej liczby argumentów (*args)
#x 20                                           #przyporządkowanie x do 1
#**kwargs {'y': 30, 'z': 10}                    #przyporządkowanie y:30, z:10 do słonnika














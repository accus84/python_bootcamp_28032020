#funkcja z wartością domyślną
def incrementator(poczatek, krok = 1):
    return poczatek + krok

#wartość domyślna
print(incrementator(10))                                #11

#nadanie wartości
print(incrementator(10, 4))                             #14

#rekurencja
def decrement(n):
    if n == 0:          #zabezpieczenie przed wieczną rekurencją, break nie ma tu zastosowania bo on działa w pętli
        print(0)        #...
        return          #teraz funkcja się zakończy
    print(n)            #to już jest inna funkcja
    decrement(n-1)

decrement(10)

#tworzenie silni za pomocą rekurencji
def silnia(n):
    if n < 0:
        return "Error"
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(5) == 120
    assert silnia(-5) == "Error"

text = "ala ma kota"

def reku_print(text):
    # nie można użyć pętli
    pass

reku_print(text)

print(silnia(4))

#def test_silnia():
#    assert silnia(0) == 0
#    assert silnia(1) == 1
#    assert silnia(2) == 2
#    assert silnia(3) == 6
#    assert silnia(5) == 120
#    assert silnia(-5) == "Error"


#DO ROZWIĄZANIA

a=[1,5,9,11,2,66]
print(a[3])                     #       5
print(a[3:])                    #       [11, 2, 66]     wszystko od elementu 3
print(a[:3])                    #1      [1, 5, 9]       wszystko do elementu 3
print(a[2::2])                  #1      [9, 2]          od elementu 2 co drugi element

print('test')

#pierwsze rozwiązanie
text = "ala ma kota"
def reku_print(text):
    if text:                    #jesli warunek true? to wykonuj
        print(text[0])          #wyprintuj element 0 a następnie
        reku_print(text[1:])    #pobierany kolejny element od 1

reku_print(text)

print('test')

#drugie rozwiązanie
def reku_print(text):
    if text == '':             #jeśli natrafisz na pusty znak czyli już poza elementami stringa, to nie może by ć wartość wpisana na sztywno bo się zmienia dynamicznie
        return
    else:
        print(text[0])
        reku_print(text[1:])

reku_print(text)

print()

def countdown(n):
  if n == 0:
    print('Blastoff!')
    return              #opcjonalne
  else:                 #opcjonalne
    print(n)
    countdown(n - 1)

countdown(5)
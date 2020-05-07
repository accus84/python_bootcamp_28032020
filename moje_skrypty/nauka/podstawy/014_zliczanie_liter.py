#przedstaw w formie słownika liczbę wystąpień danego napisu
#trzeba pamiętać, że znak =  w przypadku słowników to przypisanie wartości do klucza

napis = "ala ma kota"
zliczenia = dict() # {}

a = "cos"
slownik = {a:2}
print(slownik[a])                           #2  wypisanie samej wartości klucza a
print(slownik)                              #{'cos': 2}     wypisanie całego słownika
print(slownik.get(a,0))                     #pobieranie wartości klucza a     2       jeśli nie ma klucza a to wyświetli się 0
print(slownik.get('b',0))                   #nie ma słownika 'b' więc wyśżwietli się 0
slownik[a] = slownik[a] +1                  #dodawnie 1 do wartości klucza a
print(slownik)                              #a więc teraz słownik to {'cos': 3}
print(zliczenia)                            #{} na razie zbiór jest pusty

#pierwszy sposób
for i in napis:                             #osobno dla: a l a m a k o t a
    if i in zliczenia:                      #jeśli a jest już w słowniku zliczenia
        zliczenia[i] = zliczenia[i] + 1     #(po lewej jest klucz, po prawej jest wartość) ... to wtedy dla klucza a dodaj 1 do jego obecnej wartości
    else:
        zliczenia[i] = 1                    #a jesli nie ma jeszcze a w słowniku to ustaw wartość klucza a na 1 (bo już się pojawił pierwszy raz)
print(zliczenia)                            #na koniec wyświetl zliczenia

#drugi sposób
for i in napis:                             #osobno dla: a l a m a k o t a
    zliczenia[i] = zliczenia.get(i, 0) + 1  #jeśli a jest w słowniku to wartośćią dla a będzie wartość a, natomiast jeśli nie ma to wartością początkową będzie 0 a następnie dodanie 1
#trzeci sposób
for i in napis:
    zliczenia[i] = napis.count(i)
print(zliczenia)

#czwarty sposób przez import modułu collections
from collections import defaultdict

zliczenia = defaultdict(int)

for i in napis:
    zliczenia[i] += 1
print("333: ", zliczenia)
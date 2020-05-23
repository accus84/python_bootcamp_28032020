"""

Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:

wiecej_niz('ala ma kota a kot ma ale', 3)
{'a', ' '}

"""

text = "aaaa bbbb cccc"
#x = set(text)
# {'a', 'b', 'c', ' '}

#print(text)                                 #aaaa bbbb cccc
#print(x)                                    #{'b', ' ', 'a', 'c'}       -zbiór jest nieuporządkowany i nie ma powtórzeń
#print(text.count('a'))                      #4 liczy ile jest 'a' w zbiorze
#x.add('x')                                  #dodanie 'x' do zbioru
#print(x)                                    #{' ', 'x', 'c', 'a', 'b'}

#x.add('xxxxxxxx')

def wiecej_niz(text, prog):
    zbior = set()                           #utworzenie pustego zbioru
    for znak in set(text):                  #dla każdego znaku ze zbioru text (znaki w zbiorze są unikalne - nie powtarzają się)
        if text.count(znak) > prog:         #jeśli ten każdy znak zliczany tym razem w tekście jest większy niż określony prog...
            zbior.add(znak)                 #to dodaj ten znak do zbioru o nazwie zbior
    return zbior                            #i na koniec zwróć zbiór

print(wiecej_niz(text, 3))

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustego_napis():
    assert wiecej_niz("aaaaa bbbb ccc dd e", 0) == {'a', 'b', 'c', 'd', 'e', " "}
    assert wiecej_niz("aaaaa bbbb ccc dd e", 3) == {'a', 'b', " "}


#funkcja zwracająca znaki występujące więcej niż zadana liczba razy

text = "Lebron James jest jednym z najlepszych koszykarzy świata. Przez niektórych uważany jest za największego koszykarza w historii."

def wiecej_niz(text, x):
    wynik = set()                           #utworzenie pustego zbioru, do którego będziemy wrzucali nasz końcowy wynik
    for i in set(text):                     #na żywo text dajemy jako set żeby mieć unikaly zbiór znaków
        if text.count(i) > x:               #jeśli liczba wystąpień i w naszym tekście jest większa od podanej wartości x
            wynik.add(i)                    #to dodaj literkę i do pustego zbioru
    return wynik                            #a na koniec wyświetl zbir wynik

print(wiecej_niz(text, 10))                 #{' ', 'a'}
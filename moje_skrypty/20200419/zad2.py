#funkcja z wartością domyślną
def incrementator(poczatek, krok = 1):
    return poczatek + krok

#wartość domyślna
print(incrementator(10))

#nadanie wartości
print(incrementator(10, 4))

# Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
# Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi - odpowiednio < i >.
# Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.

def policz_znaki(text, znaki = 0):
    lista = []
    for i in list(text):
            ind_pocz = (text.index('<'))
            ind_kon = (text.index('>'))
    zakres = text[ind_pocz:ind_kon+1]
    return len(zakres)

print(policz_znaki('ala ma <kota> a kot ma ale'))

#trzeba to przerobić do drugiego wymogu

def policz_znaki(text, znaki):
    return text.index(">") - text.index("<") - 1

def policz_znaki(text, start = "<", stop = ">"):        #domyślne wartości to start jako < i stop jako >
    poziom = 0
    licznik = 0
    for znak in text:
        if znak == start:
            poziom += 1
            continue
        elif znak == stop:
            poziom -= 1
            continue
        licznik += poziom
    return licznik

print(policz_znaki("jakies <znaczki>"))
print(policz_znaki("a <a<a<a>>>"))

def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert policz_znaki('a <a<a<a>>>') == 6
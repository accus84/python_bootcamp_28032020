#podzielna przez 1 i przez siebie (zwraca tylko true albo false)
def czy_jest_pierwsza(liczba):
    for i in range (2, liczba):     #np dla 12 zakres od 2 do 12 - w ten sposób sprawdzimy czy dzieli się przez coś jeszcze (pomijamy 1 bo przecież wszysko się przez to dzieli)
        if liczba % i == 0:         #jeśli z dzielenia 12 przez 2,3,4,5,6,7,8,9,10,11 zostaje jakaś reszta to nie jest to liczba pierwsza
            return False
    return True                     #a w przeciwnym wypadku to liczba pierwsza

# określam co ma zwracać (testuje) - ważne, na rozmowie często testy są robione
#jeśli któryś z tych testów nie jest spełniony to się pojawi błąd z AssertionError
assert czy_jest_pierwsza(6)  == False
assert czy_jest_pierwsza(11) == True
assert czy_jest_pierwsza(8)  == False
assert czy_jest_pierwsza(13) == True

print(czy_jest_pierwsza(5))

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(13) == True

print(__name__)
if __name__ == "__main__":
    print("Wykonuję testy")
    assert czy_jest_pierwsza(6) == False
    assert czy_jest_pierwsza(10) == False

    print("Wszystko ok.")

# pip install pytest
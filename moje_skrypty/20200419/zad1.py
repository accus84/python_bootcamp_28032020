#Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy
#funkcja przyjmuje 2 argumenty

def wiecej_niz(text, prog):
    zbior = set()
    for znak in set(text):
        if text.count(znak) > prog:
            zbior.add(znak)
    return zbior

print(wiecej_niz("ala mamama kota", 2))
#a jest 3 razy, m jest3 razy więc powienno zwrócić {a, m}

#to poniżej tworzymy na początku, testuję co powinno zwracać
def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustegopustego_napisu():
    assert wiecej_niz("aaaaa bbb cc dd", 1) == {'a', 'b' , 'c', 'd', " "}


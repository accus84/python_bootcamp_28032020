# Zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu.

#funkcja sprawdzająca czy zakres dat jest przestępny
def lata_przestepne(x, y):
    if x < y:
        tab = []
        for i in range(x,y):
            if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
                tab.append(i)
        return tab
    else:
        print ("Nieprawidłowy zakres dat")

print(lata_przestepne(1990,2020))  #[1992, 1996, 2000, 2004, 2008, 2012, 2016]

def test_lata_przestepne():
    assert lata_przestepne(1990,2020) == [1992, 1996, 2000, 2004, 2008, 2012, 2016]
    assert lata_przestepne(395, 404) == [396, 400]



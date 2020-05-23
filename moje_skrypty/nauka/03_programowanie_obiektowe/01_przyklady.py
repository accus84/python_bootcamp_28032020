#programowanie obiektowe

#klasa - cechy, atrybuty opisujace jakis obiekt np. monitor: przekatna ekranu, rozdzielczosc, ilosc kolorow, waga, model
#klasa ludzie: mamy pewne cechy wspolne ale roznimy sie tez

class Monitor:                              #definicja klasy

    def __init__(self, brand, model):       #metoda (funkcja użyta w kontekście klasy), self przekazuje brand i model dalej (widać to w def __str__ poniżej)
        self.brand = brand
        self.model = model

    def __str__(self):                                  #dopisanie implementacji metody do definicji
        return f"<Monitor> {self.brand} | {self.model}>"                  #będzie zwracało taki napis zawsze jak wywołam tylko obiekt

##DO TEGO POWYZEJ JEST CZESC PYTHONOWA

    def wlacz(self):
        print(self, "wlacza sie")

m = Monitor("Philips", "M")                               #obiekt klasy przypisany do zmiennej m
#m2 = Monitor("Sony", "D")

print(m)                                                  #<Monitor> Philips | M>       automatycznie wywołanie metody str
#print(m2)

#atrybut obiektu
#m.brand = "Philips"
#m2.brand = "Sony"

#print(m.brand)
#m.wlacz()                                               #<Monitor> Philips | M> wlacza sie

#print(m.brand)

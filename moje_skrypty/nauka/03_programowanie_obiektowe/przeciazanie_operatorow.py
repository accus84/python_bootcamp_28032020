#przeciązanie operatorów

import math

class Kwadrat:
    def __init__(self, bok):                            #pierwszy porównywany parametr ma automatycznie klasę self, drugi trzeba zdefiniować
        self.bok = bok
    #poniżej napisanie metod żeby było wiadomo jak program ma się zachować w nietypowych operacjach (np. dodawanie do siebie kwadratów)

    #dodawanie
    def __add__(self, other):
        bok = math.sqrt(self.pole + other.pole)         #bok to dodawanie kwadratów
        return Kwadrat(bok)

    #większe niż
    def __gt__(self, other):
        return self.bok > other.bok

    def __gte__(self, other):
        return self.bok >= other.bok

    def __eq__(self, other):
        return self.bok == other.bok

    def __mul__(self, other):
        if isinstance(other, int):

            return Kwadrat(self.bok * other)
        elif isinstance(other, Kwadrat):
            return Kwadrat(self.bok * other.bok)
        else:
            raise NotImplementedError()

    def __str__(self):
        return f"<Kwadrat: {self.bok}>"

    @property
    def obowod(self):
        return self.bok * 4

    @property
    def pole(self):
        return self.bok ** 2

    def porownaj(self, other):
        return self.bok == other.bok

kw1 = Kwadrat(4)
kw2 = Kwadrat(5)
kw3 = Kwadrat(4)
print(kw1.pole)                                 #16
print(kw2.pole)                                 #25
# self + other
wynik = kw1 + kw2
print(wynik)                                    #<Kwadrat: 6.4031242374328485>
print(kw1 < kw2)                                #True
print(kw1 + kw3)                                #<Kwadrat: 5.656854249492381>
print(kw1 == kw3)                               #True
print(kw1.__eq__(kw3))                          #True
print(kw1.porownaj(kw3))                        #True
print(kw1 * 3)                                  #<Kwadrat: 12>
print(kw1 * kw2)                                #<Kwadrat: 20>

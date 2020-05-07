kolekcja = [(10, "z"), (5, "c"), (15, "a")]

#sortowanie po pierwszym elemencie czyli 5,10,15
print(sorted(kolekcja))

#sortowanie po drugim elemencie czyli 5,10,15
def second(x):
    return x[1]

print(sorted(kolekcja, key=second))
#to samo z pominięciem dodatkowej funkcji second()
print(sorted(kolekcja, key=lambda x: x[1]))         #lambda <agument który wchodzi>: <argument który wychodzi>
#dla lambda innt przykład lambda x, y: x + y        (wchodzi x i y, wychodzi x + y)

#zadanie
lista_osob = ["Jan Nowak", "Anna Zagajska", "Mateusz Pospieszalski", "Piotr Baron"]
print(sorted(lista_osob, key = lambda x: x.split()[1]))         #split podzielił Jan Nowak itd na 2 części
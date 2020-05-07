#lambda x: x....
#lambda umożliwia operacje na samym sobie
kolekcja = [(10, "z"), (5, "c"), (15, "a")]

#sortowanie po drugim elemencie czyli 5,10,15

def first(x):
    return x[0]

def second(x):
    return x[1]

#sortowanie po pierwszym elemencie czyli 5,10,15
print(first(kolekcja))                              #(10, 'z')   funkcja zwracająca element 0 listy kolekcja
print(second(kolekcja))                             #(5, 'c')   funkcja zwracająca element 1 listy kolekcja

print(sorted([5,7,14,-2]))                          #[-2, 5, 7, 14]     domyślne sortowanie
print(sorted(kolekcja))                             #[(5, 'c'), (10, 'z'), (15, 'a')]   domyślne sortowanie po elemencie 0
#sorted ma parametr key, który jest używany do wywołania jakiejś funkcji
print(sorted(kolekcja, key=first))                  #[(5, 'c'), (10, 'z'), (15, 'a')]   sortowanie listy kolekcja według funkcji first (funkcja first zwraca element 0)
print(sorted(kolekcja, key=second))                 #sortowanie(co, jak)    [(15, 'a'), (5, 'c'), (10, 'z')]   - posortowanie po elemencie 1 czyli a c z
#to samo, można rozpatrywać jako przetwórz x: tak aby pobrać element 1 x
print(sorted(kolekcja, key=lambda x: x[1]))         #lambda <agument który wchodzi>: <argument który wychodzi>   otrzymamy (5, 'c')

#inny przykład
suma = lambda x, y: x + y
print(suma(1, 2))                           #suma 1 i 2
print((lambda x, y: x + y)(1, 2))           #suma 1 i 2


#zadanie
lista_osob = ["Jan Nowak", "Anna Zagajska", "Mateusz Pospieszalski", "Piotr Baron"]
print(sorted(lista_osob, key = lambda x: x.split()[1]))         #split podzielił Jan Nowak itd na 2 części      sortowanie po nazwisku czyli: sortowanie(lista_osob, dzielenie samego siebie i branie po uwagę elementu 1)
#['Piotr Baron', 'Jan Nowak', 'Mateusz Pospieszalski', 'Anna Zagajska']

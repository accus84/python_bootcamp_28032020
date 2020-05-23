# listy

elementy = [1, 2, 3, 4, 5, "xx", 2.0, 2]

# print(sum(elementy))
i = 0
while i < len(elementy):
    print(elementy[i])                      #wypisz po kolei każdy element
    i += 1
print("-" * 40)                             #na koniec utwórz linię "-" o długości 40

print()

for xx in elementy:
    print(xx, end = '')                     #12345xx2.02

print()

licznik = 0
for i in "123":
    licznik += 1
    print(licznik)                          #1, 2, 3
print(licznik)                              #3

print()

lista = ["A", 'B', 'C', 'D']
print(lista.index('C') - lista.index('A'))  #indexem 'C' jest 3, indexem 'A' jest 1 zatem wynik to 3 - 1 = 2

print()

i = 0
while i < 10:
    index = i % 4                           # reszta 0/4 to 0, reszta 1/4 to 1, reszta 2/4 to 2, reszta 3/4 to 3, reszta 4/4 to 0, reszta 5/4 to 1 reszta 6/4 to 2 itd
    print(i, lista[index])                  #prinr(0,lista[0]), print(1,lista[1], p\print(2,lista[2], print(3,lista[3], print(4,lista[0], print(5,lista[1] itd
    i += 1





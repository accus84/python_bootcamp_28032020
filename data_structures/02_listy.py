#lista jest mutowalna
elementy = [1, 2, 3, "xxx", 22.04, "ala"]
print(type(elementy))           #jaki to jest typ
#dodanie elementu do listy
elementy.append("cos")
#zwraca długość listy
print(len(elementy))

for element in elementy:
    print(element)

for x in "abc":
    if x == 'b':
        break       #break wychodzi z pętli, continue pomija jeden obrót pętli
    print(x)

for y in "123":
    for x in "abc":
        if x == "b":
            break   #wyjśćie ALE TYLKO Z PĘTLI ZAGNIEŻDŻONEJ
        print(x + y)

lista = [1, 4, 5, 7]
for i in lista:
    print(i)
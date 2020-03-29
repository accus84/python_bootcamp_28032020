#lista jest mutowalna
elementy = [1, 2, 3, "xxx", 22.04, "ala"]
print(type(elementy))           #jaki to jest typ
#dodanie elementu do listy
elementy.append("cos")
#zwraca długość listy
print(len(elementy))

while len(elementy < 11:
    elementy.append("xx"))
print(elementy)
#zbiory, w zbiorze elementy są nieuporządkowane więc nie ma indeksów
#zbiory są tylko do tego czy coś jest w zbiorze, jaka jest część wspólna zbioru itd
#suma |
#różnica -
#iloczyn &
#różnica symetryczna

# pusty zbior
zbior = set()
#dodanie do zbioru
zbior.add(1)
zbior.add("x")
print(zbior)
#literowanie po zbiorze
for element in zbior:
    print(element)

#inne metody:
#print(dir(zbior))

#tworzenie zbioru
a = {1, 2, 3}
b = {2, 3, 4}
#suma (tylko wspólne)
print(a | b)
#część wspólna
print(a & b)
#różnica
print(a - b)
#różnica symetryczna, takie elementy które nie są w części wspólnej
print(a ^ b)
#usuwanie randomowego elementu
print(a.pop())
print(a)
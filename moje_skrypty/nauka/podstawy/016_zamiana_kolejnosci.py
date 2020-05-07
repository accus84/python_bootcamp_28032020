#jk mamy listę to chcemy zmienić kolejność elementów żby były uporządkowane od najmniejszego do najwiuększego

#pierwszy sposób przez moduł sort
lista = [9, 1, 6, 8, 4, 3, 2, 0]
lista.sort()
print(lista)
#kartka_sort = sorted(lista, key = lambda x: x[0])
#sortowawnie przez wybieranie
#BĘDZIE NA KARTKÓWCE

#drugi sposób
lista = [9, 1, 6, 8, 4, 3, 2, 0]
print(min(lista))           #wartość minimalna listy
lista.remove(min(lista))
print(lista)
def sortowanie(n):          #funkcja sortująca podaną listę
    b = []                  #pusta lista
    while n != []:          #jeśli lista nie jest pusta
        x = min(n)          #x to wartość minimalna listy (czyli 0)
        n.remove(x)         #usunięcie x z listy (teraz lista = [9, 1, 6, 8, 4, 3, 2])
        b.append(x)         #do pustej listy dodawana jest każda kolejna minimalna wartść, która została jeszcze w liście czyli odpowiednio 0, 1, 2, 3, 6, 8, 9
    return b

print(sortowanie(lista))

#trzeci sposób - sortowanie przez wybieranie
lista = [6, 8, 1, 0, 15, 4, 5, 12, 14, 3]
for i in range(len(lista)):                 # długość 8, zajmujemy się każdym z zlementów tej listy
    k = i                                   # potrzebne tylko do następnej pętli, gdzie element i to jest to samo co element k
    for z in range(i + 1, len(lista)):      # zakres 1-8
        if lista[z] < lista[k]:             # teraz wewnątrz jeśli kolejny element z listy jest mniejszy od poprzedzającego
            k = z                           # to ten kolejny element zajmuje miejsce poprzedniego
    # a, b  = b, a                          # szybka zamiana a i b
    lista[i], lista[k] = lista[k], lista[i] # zamiana elementu poprzedniego z kolejnym
print(lista)

#funkcja
lista = [-5, 0, 12, 5, 16, 6, 4, -3]
def sort (l):
    a = []
    while l != []:
        x = min(l)
        l.remove(x)
        a.append(x)
    return a

print(sort(lista))

#sortoanie przez wybieranie + funkcja
lista = [-5, 0, 12, 5, 16, 6, 4, -3]
for i in range(len(lista)):
    for k in range(i+1, len(lista)):
        if lista[k] < lista[i]:                         #jeśli k (czyli następna liczba) jest mnejsza niż pierwsza to zamiań
            lista[k], lista[i] = lista[i], lista[k]
print(lista)

def sortowanie(l):
    for i in range(len(l)):
        for k in range(i + 1, len(l)):
            if l[k] < l[i]:                             # jeśli k (czyli następna liczba) jest mnejsza niż pierwsza to zamiań
                l[k], l[i] = l[i], l[k]
    print(l)

jakas_lista = [-6, 7, 9, 3]

sortowanie(jakas_lista)                                 #[-6, 3, 7, 9]
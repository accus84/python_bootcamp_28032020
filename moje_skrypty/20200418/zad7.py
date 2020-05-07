#jk mamy listę to chcemy zmienić kolejność elementów żby były uporządkowane od najmniejszego do najwiuększego
#TO ZADANIE BĘDZIE NA KARTKOWCE
lista = [9, 1, 6, 8, 4, 3, 2, 0]
lista.sort()
print(lista)
#kartka_sort = sorted(lista, key = lambda x: x[0])
#sortowawnie przez wybieranie
#BĘDZIE NA KARTKÓWCE

lista = [9, 1, 6, 8, 4, 3, 2, 0]

def sortowanie(n):
    b = []                  #pusta lista
    while n != []:
        x = min(n)
        n.remove(x)
        b.append(x)
    return b

print(sortowanie(lista))

#sortowanie przez wybieranie
#TO BĘDZIE NA KIARTKÓWCE
lista = [6, 8, 1, 0, 15, 4, 5, 12, 14, 3]
for i in range(len(lista)):                 # długość 8, zajmujemy się każdym z zlementów tej listy
    k = i                                   # potrzebne tylko do następnej pętli, gdzie element i to jest to samo co element k
    for z in range(i + 1, len(lista)):      # zakres 1-8
        if lista[z] < lista[k]:             # teraz wewnątrz jeśli kolejny element z listy jest mniejszy od poprzedzającego
            k = z                           # to ten kolejny element zajmuje miejsce poprzedniego
    # a, b  = b, a                          # szybka zamiana a i b
    lista[i], lista[k] = lista[k], lista[i] # zamiana elementu poprzedniego z kolejnym
print(lista)


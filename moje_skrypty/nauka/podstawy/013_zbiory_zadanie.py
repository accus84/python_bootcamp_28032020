#sortowanie przez wybieranie
#uporządkuj listę

#pierwsza pętla i - sprawdzanie dla elementu[0]: czy element[1] <element[0], czy element [2] < element[0] czy element[3] < element[0] itd
#po pierwszej pętli dla i mamy zapewnioną najmniejszą wartość dla elementu[0]
#po pierwszej pętli: [0, 1, 6, 8, 15, 4, 5, 12, 14, 3]
#druga pętla i - sprawdzanie dla elementu[1]: czy element[2] <element[1], czy element [3] < element[1] czy element[4] < element[1] itd
#po drugiej pętli dla i mamy zapewnioną najmniejszą wartość dla elementó[0,1]
#po drugiej pętli: [0, 1, 6, 8, 15, 4, 5, 12, 14, 3]
#trzecia pętla i - sprawdzanie dla elementu[2]: czy element[3] <element[2], czy element [4] < element[2] czy element[5] < element[2] itd
#po trzeciej pętli dla i mamy zapewnioną najmniejszą wartość dla elementó[0,1,2]
#po trzeciej pętli: [0, 1, 3, 4, 6, 8, 15,, 5, 12, 14]
#...

lista = [6, 8, 1, 0, 15, 4, 5, 12, 14, 3]
for i in range(len(lista)):                 # długość 10, zajmujemy się każdym z zlementów tej listy
    k = i                                   # potrzebne tylko do następnej pętli, gdzie element i to jest to samo co element k
    for z in range(i + 1, len(lista)):      # zakres 1-10
        if lista[z] < lista[k]:             # teraz wewnątrz jeśli kolejny element z listy jest mniejszy od poprzedzającego
            k = z                           # to ten kolejny element zajmuje miejsce poprzedniego
    # a, b  = b, a                          # szybka zamiana a i b
    lista[i], lista[k] = lista[k], lista[i] # zamiana elementu poprzedniego z kolejnym
print(lista)

print()

cyfry = [5, 1, 4]
for i in range(len(cyfry)):                 # zakres długości na 3 zaczynając od 0 czyli i=0, i=1, i=2
    k = i                                   # teraz k=0, k=1, k=2
    for z in range(i + 1, len(cyfry)):      #pierwszy obrót (i=0): z jest w zakresie (0+1, 3) czyli w zakresie 1, 2 czyli z=1, z=2
        if cyfry[z] < cyfry[k]:             # jeśli cyfry[1] jest mniejsze od cyfry[0] czyli jak w naszym przypadku 1 < 5
            k = z                           # z (1) nadaje wartość zmiennej k (teraz k =1)
    # a, b  = b, a
    cyfry[i], cyfry[k] = cyfry[k], cyfry[i] # cyfry[0], cyfry [1] = cyfry[1], cyfry[10]     - zamiana cyfr
print(cyfry)

#uporządkuj rosnąco
l = [5, -3, 0, 14, 9, -5]
for i in range(len(l)):
    for k in range(i +1 , len(l)):
        if l[k] < l[i]:
        #jeśli następna cyfra mniejsza od cyfry o indeksie 0
            l[i], l[k] = l[k], l[i]             #to zamień
print(l)

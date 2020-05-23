#Wypisz liczby parzyste ze stworzonego przez Ciebie zbioru

zbior = set()

while True:
    polecenie = input("Wpisz liczbę lub k by zakończyć: ")
    if polecenie == "k":
        break
    zbior.add(int(polecenie))

#szybkie wypisywanie liczb pacrzystych (zakres od 0 do 100 co 2)
liczby_parzyste = set(range(0, 101, 2))                                 #ustalamy sobie zbiór od 0 do 100 ale tylko co 2 więc są tu liczby parzyste od 0 do 100


print(f"Unikalnych liczb: {len(zbior)}")                                #długość zbioru to inaczej liczba elementów w zbiorze, wyświetlamy bez obaw zbiór bo posiada tylko unikalne wartości
print(f"Parzystych z zakresu 1-100: {len(zbior & liczby_parzyste)}")    #długość części wspólnej naszego zbioru i liczb parzystych


# wypisz sumę elementów listy i zbioru
elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
elementy2 = {"aaa", "aba", "ccc"}
print(elementy2 & set(elementy))

#czy podzbiór issubset
first_set = {27, 43, 34}
second_set= {34, 93, 22, 27, 43, 53, 48}
print(dir(first_set))
print(first_set.issubset(second_set))




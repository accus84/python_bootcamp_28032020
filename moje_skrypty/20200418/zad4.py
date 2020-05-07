#napisz prog zliczający liczbę unikalnych liczb wprowadzonych przez usera. Sprawdź jak dużo z tych liczb jest l parzystymi w zakresie 1-100
zbior = set(input("Podaj liczbe: "))

while True:
    polecenie = input("Wpisz liczbę lub k aby zakończyć ")
    if polecenie =="k":
        break
    zbior.add(int(polecenie))
liczby_parzyste = set(range(0, 101, 2))      #zaczynamy od 0, konczymy na 101, co 2 element

print(zbior)
print(liczby_parzyste)
print(zbior & liczby_parzyste)

print(f"Unikalnych liczb jest {len(zbior)}")
print(f"Parzystych liczb jest {len(zbior & liczby_parzyste)}")


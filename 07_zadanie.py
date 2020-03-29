#czy podana liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7
liczba = int(input("Podaj liczbę: "))
print()
print(f"Czy podana liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7? {(liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7 }")
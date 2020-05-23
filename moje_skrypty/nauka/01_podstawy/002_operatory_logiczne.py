#czy liczba większa od 10, mniejsza od 15 i podzielna przez 2

liczba = 11
print(liczba > 10 and liczba < 15 and liczba % 2 == 0)
#AND - true jest tylko wtedy gdy wszystkie warunki są spełnione
#OR - true gdy przynajmniej jeden warunek jest spełniony

#czy podana liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7
liczba = int(input("Podaj liczbę: "))
print()
print(f"Czy podana liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7? {(liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7 }")
miasto_a = input("podaj nazwę miasta a: ")
miasto_b = input("podaj nazwę miasta b: ")
cena_za_km = float(input("Podaj cenę za km: "))
dystans = int(input(f"Podaj dystans pomiędzy miastami {miasto_a}-{miasto_b}:"))
spalanie = float(input ("Podaj spalanie"))

#jakie spalanie na 1 km
spalanie_na_km = int(spalanie) / 100

koszt = dystans * cena_za_km * spalanie_na_km

print(f"Miasto a: {miasto_a}")
print(f"Miasto b: {miasto_b}")
print(f"Dystans: {miasto_a}-{miasto_b}: {dystans}")
print(f"Koszt przejazdu z {miasto_a} do {miasto_b} wynosi {koszt} zł")
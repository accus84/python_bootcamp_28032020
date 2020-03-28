miasto_a=input("podaj nazwę miasta a: ")
miasto_b=input("podaj nazwę miasta b: ")
dystans = 420

cena_za_km = 4.55
#jakie spalanie na 1 km
spalanie_na_km = 5.5 / 100

koszt = int(dystans * cena_za_km * spalanie_na_km)

print(f"Miasto a: {miasto_a}")
print(f"Miasto b: {miasto_b}")
print(f"Dystans: {miasto_a}-{miasto_b}: {dystans}")
print(f"Koszt przejazdu z {miasto_a} do {miasto_b} wynosi {koszt} zł")
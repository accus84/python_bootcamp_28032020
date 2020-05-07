produkty = {
    "ziemniaki": 2.25,
    "pomiodory": 4.15,
    "cebula": 1.99,
    "kalafior": 3.20
}
magazyn = {
    "ziemniaki": 10,
    "pomiodory": 10,
    "cebula": 10,
    "kalafior": 10
}

print(produkty.get("ziemniaki"))        # wypisuje wartość danego słownika, jeśli nie ma takiego słownika to wpisywana jest wartość domyślna None       2.25
print(produkty.get("ziemie", 100))      # wypisuje wartość danego słownika, jeśli nie ma takiego słownika to wpisywana jest wartość 100                 100
print(produkty.values())                # wypisuje same wartości                                                                                        dict_values([2.25, 4.15, 1.99, 3.2])
print(produkty.keys())                  # wypisuje same słowniki                                                                                        dict_keys(['ziemniaki', 'pomiodory', 'cebula', 'kalafior'])
print(produkty.items())                 # wypisuje wszystko ze słownika produkty                                                                        dict_items([('ziemniaki', 2.25), ('pomiodory', 4.15), ('cebula', 1.99), ('kalafior', 3.2)])

for i in produkty:                      # wypisuje tylko słowniki za pomocą pętli
    print(i, end = ' ')                 #ziemniaki pomiodory cebula kalafior

print()

for i in produkty.items():              # wypisuje wszystko ze słownika produkty za pomocą pętli
    print(i, end = ' ')                 #('ziemniaki', 2.25) ('pomiodory', 4.15) ('cebula', 1.99) ('kalafior', 3.2)

print()

for a, b in produkty.items():           # to samo z rozbiciem na klucz i wartość klucza
    print(a, b)


#     a, b  = i
#     print(a, b)
#a, b = "k", "v"
#[("k", "v"), ()]

print()

while True:
    komenda = input("Co chcesz zrobić? [k-kup] [z-zakończ] [m-magazyn]: ")

    if komenda == "z":
        break
    elif komenda == "k":
        print("Nasz zielnik oferuje: ")
        for nazwa, cena in produkty.items():
            print(f" - {nazwa} w cenie: {cena} PLN (stan: {magazyn[nazwa]})")

        produkt = input("Co chcesz kupić? ")

        if produkt in produkty:
            ile = input(f"Ile chcesz kupić [{produkt}]? ")
            ile = float(ile)
            if ile < magazyn[produkt]:                      #magazyn[produkt] to np magazyn["ziemniaki"] co daje 10
                print(f"Za {ile} kg {produkt} zapłacisz {ile * produkty[produkt]:.2f}")
                magazyn[produkt] = magazyn[produkt] - ile
            else:
                print("Nie mamy tyle produktu")
    elif komenda == "m":
        produkt = input("Co dodajemy? ")
        ile = int(input(f"Ile dodajemy [{produkt}]? "))
#       magazyn[produkt] = magazyn[produkt] + ile           #nie można użyć = magazyn[produkt] bo jeśli takiego produktu jeszcze nie było w magazynie to wyrzuci błąd,
        magazyn[produkt] = magazyn.get(produkt, 0) + ile    #magazyn[produkt] to np magazyn["ziemniaki"] co daje 10 = 0 jeśli w magazynie nie było produktu + ile
        if produkt not in produkty:
            cena = float(input(f"Jaka cena za [{produkt}]"))
            produkty[produkt] = cena

    else:
        print("Niezrozumiała komenda")
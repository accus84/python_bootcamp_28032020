#Napisz program obsługujący bazę danych pracowników. W bazie danych przechowuj imię, nazwisko, email, rok urodzenia, pensję
#skorzystaj z modułu json
#json informacje na stronie -wpisać np "nrodowy bank polski API" - tam powinno być jak uzyskać informacje z jsona, generalnie szukać API

import json
try:
    with open("employees.json") as fp:
        lista = json.load(fp)
except FileNotFoundError:
    lista = []
komenda = input("Co chcesz zrobić? [d- dodaj, w-wypisz]: ")
if komenda == "d":
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_ur = int(input("Podaj rok urodzenia: "))
    pensja = input("Podaj pensję: ")
    email = input("Podaj email: ")
    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_ur": rok_ur,
        "pensja": pensja,
        "email": email
    }
    lista.append(pracownik)
    with open("employees.json", "w") as fp:
        json.dump(lista, fp)
elif komenda == "w":
    print("Pracownicy: ")
    for i, emp in enumerate(lista, start=1):
        print(f" - [{i}] {emp['imie']} {emp['nazwisko']} - rok: {emp['rok_ur']}, pensja: {emp['pensja']} PLN")
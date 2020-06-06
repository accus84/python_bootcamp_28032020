#klakulator walut
import requests
import json

resp = requests.get("https://api.nbp.pl/api/exchangerates/tables/A?format=json")
print(resp.json())
x = resp.json()

komenda = input("Co chcesz zrobić? [s- sprzedaj walutę, k- kup walutę, z - zakończ program]: ")


if komenda == "z":
    print("Zakończenie programu")

elif komenda == "s":
    waluta = input("Podaj nazwę lub symbol waluty ")


elif komenda == "k":
    waluta = input("Podaj nazwę lub symbol waluty ")

else:
    print("Nieprawidłowa komenda")





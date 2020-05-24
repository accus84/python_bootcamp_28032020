#f = open("data/logs.txt")
#print(f.read())

#prawidłowa metoda - do odczytu
with open("data/logs.txt") as f:
    print(f.read())

with open("data/przykladowy_plik.txt", "w") as f:           #w katalogu data utworzy się plik tekstowy przykladowy_plik.txt
    f.write("Ala ma kota. kot ma Alę")
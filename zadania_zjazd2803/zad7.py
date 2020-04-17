# Napisz program który obliczy stan konta za N lat, gdzie stan początkowy konta wynosi SPK,
# a stopa oprocentowania P% rocznie (obowiązuje roczna kapitalizacja odsetek). N, SPK i P podaje użytkownik programu.

n = int(input("Podaj liczbę lat: "))
spk = float(input("Podaj stan początkowy: "))
p = float(input("Podaj stopę procentową: "))

p = p * 1 / 100
konto = spk * ((1 + p / 1) ** n)
print(konto)

#Napisz program obliczający średnią wartość podanych przez użytkownika liczb
# Pozwól na wprowadzenie max 10 liczb. Skorzystaj z funkcji sum()
tablica = []
licznik = 1
while licznik < 11:
    element = int(input(f"Podaj liczbę numer {licznik}: "))
    tablica.append(element)
    licznik += 1
print(f"Suma z {len(tablica)} liczb wynosi {sum(tablica)}")
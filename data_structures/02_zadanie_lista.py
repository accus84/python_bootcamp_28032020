#Napisz program obliczający średnią wartość podanych przez użytkownika liczb
# Pozwól na wprowadzenie max 10 liczb. Skorzystaj z funkcji sum()
tablica = []
while len(tablica) < 10:
    element = int(input(f"Podaj liczbę: "))
    tablica.append(element)
print(f"Suma z {len(tablica)} liczb wynosi {sum(tablica)}")
print(f"Średnia z {len(tablica)} liczb wynosi {sum(tablica) / len(tablica)}")
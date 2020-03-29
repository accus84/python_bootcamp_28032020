#Napisz program obliczający średnią wartość podanych przez użytkownika liczb
# Pozwól na wprowadzenie max 10 liczb. Skorzystaj z funkcji sum()
tablica = []
counter = 1
while counter < 11:
    element = int(input(f"Podaj liczbę numer {counter}: "))
    tablica.append(element)
    counter += 1
print(f"Suma z {len(tablica)} liczb wynosi {sum(tablica)}")
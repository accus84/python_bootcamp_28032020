#Napisz program obliczający średnią wartość podanych przez użytkownika liczb
# Pozwól na wprowadzenie max 3 liczb. Skorzystaj z funkcji sum()
#tablica = []
#while len(tablica) < 3:
#    element = int(input(f"Podaj liczbę: "))
#    tablica.append(element)
#print(f"Suma z {len(tablica)} liczb wynosi {sum(tablica)}")
#print(f"Średnia z {len(tablica)} liczb wynosi {sum(tablica) / len(tablica)}")


#Napisz program zliczający wystąpienie liczb dodatnich i ujemnych w liście
dodatnie = 0
ujemne  = 0
dane = [10, 20, -30, -500, 4, -220]
for i in dane:
    if i >= 0:
        dodatnie += 1
    else:
        ujemne += 1

print(f"W liście jest {dodatnie} liczb dodatnich i {ujemne} liczb ujemnych")


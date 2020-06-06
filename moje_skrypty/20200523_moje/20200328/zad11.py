#Napisz program wypisujący na konsolę tabliczkę mnożenia dla liczb 0-9 w postaci tabelki
for i in range(10):         #zwraca pętle od 0 do 9
    print(f"{i:4}", end= "")      #zwraca w tej samej linii o szerokości 4
print()
print()
for i in range(10):
    print(i, end="    ")
    for j in range(10):

        print(f"{i*j:4}", end="")

    print()

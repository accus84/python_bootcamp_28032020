#Napisz program, który wczyta od użytkownika tekst, a następnie podwoi w nim co drugi znak i wyświetli wynik

text = input("Podaj jakiś tekst: ")
text_split = text.split(" ")
for i in text_split:
    print(i[0:1] + i[1]*2 + i[2:], end = " ")

text = input("Podaj jakiś tekst: ")



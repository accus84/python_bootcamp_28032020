#Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie, np.:

#>? HELLO STRANGER!
#H L O S R N E !
#E L T A G R

text = input("Podaj jakiś tekst: ")
print(text[0::2])   #od zerowego co drugi element
print(text[1::2])   #od pierwszego co drugi element
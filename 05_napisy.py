napis = "Koronawirus"
#metoda index służy do sprawdzania numeru indexu w stringu
#wypisanie indexu 0 zmiennej napis:
print(napis[0])
#a teraz na odwrót, wypisanie pod jakim indexem jest litera K
print(napis.index("K"))
#a teraz pod jakim indexem jest litera p - pojawi się błąd bo nie ma takiego znaku w zmiennej napis
#print(napis.index("p"))
#liczenie od końca czyli od prawej do lewej
#pierwszy element od końca
print(napis[-1])
#drugi elemend od końca
print(napis[-2])
#wycinanie od 0 do 3 (bez 3)
print(napis[0:3])
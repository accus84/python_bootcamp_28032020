napis = "Koronawirus"

print(dir(napis))                       #metody ma napis
print(napis.index("o"))                 #jakie miejsce indeksu zajmuje znak 'o'
print(napis.rindex("o"))                #jesli o jest więcej niż q raz to losowe miejsce indeksu (może być 1 lub 3)
print(napis[0])
print(napis[1:])                        #wykonywana dalsza część od elementu 1
print(napis[4])
print(napis[10])
# print(napis[11])
print(napis[-1])                        #co się kryje pod index -1 (ostatni element)
print(napis[-3])
print(napis[3:7])                       #wycinanie od 3 do 7 (bez 7)

print()

## łączenie napisów - konkatenacja
n1 = "Ala"
n2 = "kot"

print(n1 + " " + n2)
# ctrl + alt + L

print(f"{n1} {n2}")                     #Ala kot
print("{} {}".format(n1, n2))           #Ala kot
print("{} {}".format(n2, n1))           #Ala kot
print("{a} {b}".format(b=n2, a=n1))     #kot Ala

print()

text = "tekst"
print(f"{text:>1}")                     #tekst  rozciągnięcie tekstu na 1 znak (sam tesk ma 5 znaków więc jest to ignorowane)
print(f"{text:>10}")                    #     tekst (ogółem od lewej 10 znaków)

print("%s %s" % (n1, n2))               #Ala kot
print("test")
print(f"{n1:>10} {n2:^5}")              #       Ala  kot      10 znaków od lewej do słowa "Ala' włącznie, 5 znaków od lewej po "Ala' do końca słowa 'kot' włącznie
print(f"{n1:>10} {n2:^10}")              #       Ala    kot     na ile znaków ma zajmować od lewej strony (jesli sam znak jest dłuższy to jest to ignorowane)
print(f"{n1:>10} {n2:>10}")              #       Ala    kot     na ile znaków ma zajmować od lewej strony (jesli sam znak jest dłuższy to jest to ignorowane)

print()

print(f"{n1:>10} {n2:^15}")             #  Ala    kot

print(f"{n1:>5} {n2:>10}")              #Ala        kot
x = 10/3
print(f"{x:.4f}")                       #wypisanie 3.3333 (cztery znaki po kropce)
print("{:>10} {:^20}".format(n2, n1))

napis = "Ala Ma kota"

#zaokrąglanie wartości
x = 20.12313

print(round(x, 2))                      #zaokrąglenie wartości do 2 miejsc po kropce    20.12
print(f"{x:.2f}")                       #zaokrąglenie wartości do 2 miejsc po kropce    20.12

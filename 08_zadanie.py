#Napisz program który na podstawie opakowania obliczy jego objętość oraz sprawdzy czy jest większa od 1 litra (100cm3)
#V = a * b * h
dlugosc = int(input("Podaj dlugosc: "))
szerokosc = int(input("Podaj szerokosc: "))
wysokosc = int(input("Podaj wysokosc: "))
print()
print(f"""
Czy objętość większa od 1 litra? {dlugosc * szerokosc * wysokosc > 100}   
""")
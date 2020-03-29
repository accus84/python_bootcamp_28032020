#Napisz program który na podstawie opakowania obliczy jego objętość oraz sprawdzi czy jest większa od 1 litra (100cm3)
#V = a * b * h
dlugosc = int(input("Podaj dlugosc: "))
szerokosc = int(input("Podaj szerokosc: "))
wysokosc = int(input("Podaj wysokosc: "))
print()
print(f"""
Czy objętość jest większa od 1 litra? {dlugosc * szerokosc * wysokosc > 1000}   
""")
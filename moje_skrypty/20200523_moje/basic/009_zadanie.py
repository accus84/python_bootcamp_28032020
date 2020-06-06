#Napisz program, który sprawdzi pełnoletność osoby na podst roku urodzenia
import datetime
current_year = int(datetime.datetime.now().year)        #zwraca obecny rok
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = current_year - rok_urodzenia
if wiek >= 18:
    print("Osiągnąłeś pełnoletność")
else:
    print("Nie jesteś pełnoletni")
#if else
x =  8
if x > 10:                  #jeśli spełnione to dalsza część nie jest sprawdzana
    print("Większy")
elif x % 2 == 0:
    print("Parzysty")
else:
    print("Żaden z warunków nie jest spełniony")

    
#Napisz program, który sprawdzi pełnoletność osoby na podst roku urodzenia
import datetime
current_year = int(datetime.datetime.now().year)        #zwraca obecny rok
rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = current_year - rok_urodzenia
if wiek >= 18:
    print("Osiągnąłeś pełnoletność")
else:
    print("Nie jesteś pełnoletni")


#Napisz program, który na podstawie liczb obliczy wynik zadanej operacji (dod, odejm, mn, dziel).
#W przypadku podania nieprawidłowej operacji progam ma wyświetlić odpowiedni komunikayt o błędzie

liczba_a = int(input("Podaj pierwszą liczbę: "))
liczba_b = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj rodzaj operacji: ")

if operacja == "+":
    print(f"Wynik {liczba_a + liczba_b}")
elif operacja == "-":
    print(f"Wynik {liczba_a - liczba_b}")
elif operacja == "*":
    print(f"Wynik {liczba_a * liczba_b}")
elif operacja == "/":
    if liczba_b != 0:
        print(f"Wynik {liczba_a / liczba_b}")
    else:
        print(f"Nie można dzielić przez {liczba_b}")
else:
    print("Nie ma takiej operacji")
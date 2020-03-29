#Napisz program, który na podst liczb obliczy wynik zadanej operacji (dod, odejm, mn, dziel).
# W przypadku podania niepraw operacji progam ma wyświetlić odp komunikayt o błędzie
""""
text = "ala"
if text =="ala":
    print("To jest ten tekst")
"""

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
    print(f"Wynik {liczba_a / liczba_b}")
else:
    print("Nie ma takiej operacji")
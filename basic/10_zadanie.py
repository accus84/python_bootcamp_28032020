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
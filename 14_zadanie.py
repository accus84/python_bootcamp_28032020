#Napisz program wyświetlający min i maks liczbę z wszystkich liczb wprowadzonych przez użytkownika.
#Daj użytkownikownikowi możliwość zakończenia wprowadzania liczb jedną komendą.
# Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby
min_x = None
max_x = None


while True:
    liczba = input("Wprowadz liczbę lub x aby zakończyć działanie programu ")
    if liczba == "x":
        break
    liczba = int(liczba)
    if min_x is None or liczba < min_x:
        min_x = liczba
    if max_x is None or liczba > max_x:
        max_x = liczba


print(f"Wartość maksymalna: {max_x}")
print(f"Wartość minimalna: {min_x}")



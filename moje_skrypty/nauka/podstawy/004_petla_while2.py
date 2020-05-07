#Napisz program wyświetlający min i maks liczbę z wszystkich liczb wprowadzonych przez użytkownika.
#Daj użytkownikownikowi możliwość zakończenia wprowadzania liczb jedną komendą.
# Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby
min_x = None
max_x = None


while True:                                 #pętla wykonuje się nieokreśloną ilość razy - break działa tylko z pętlą for albo while dlatego tu stosujemy pętlę
    liczba = input("Wprowadz liczbę lub x aby zakończyć działanie programu ")
    if liczba == "x":
        break                               #jeśli liczbą jest x to jest zakończenie programu
    liczba = int(liczba)                    #a jak nie to już jest jakaś wprowadzona liczba, musi być zmiana ze str na int
    if min_x is None or liczba < min_x:     #if ... is None powoduje że cokolwiek wpiszemy to zamiast None...
        min_x = liczba                      #liczba zostanie przypisana do min_x
    if max_x is None or liczba > max_x:
        max_x = liczba

print(f"Wartość maksymalna: {max_x}")
print(f"Wartość minimalna: {min_x}")
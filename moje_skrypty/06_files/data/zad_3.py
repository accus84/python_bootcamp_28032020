#Napisz program wczytująy listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością
#Wejsciowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter, linie zawierające białe znaki oraz błędne adresy email
#(brak znau @ lub występuje on wiele razy).
#Wynikowy plik powinien zawierać unikalne, posortowane, poprawne adresy email
#Przykład:
#python clean_email.py emails.txt cleaned_emails.txt

import sys

try:
    f_path = sys.argv[1]                #pierwszy argument wczytywany z terminala
    f2_path = sys.argv[2]
except KeyError:
    f_path = "data/emails.txt"          #drugi argument wczytywany z terminala
    f2_path="data/cleaned_emails.txt"

with open(f_path, "r") as f:
    lines = f.readlines()
    lines = sorted(lines)
    if lines[0].isupper:
        print(lines[0])
    f.close()

with open (f2_path, "w") as f:
    f.writelines(lines)
    f.close()
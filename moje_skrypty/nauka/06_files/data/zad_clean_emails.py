#Napisz program wczytująy listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością
#Wejsciowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter, linie zawierające białe znaki oraz błędne adresy email
#(brak znau @ lub występuje on wiele razy).
#Wynikowy plik powinien zawierać unikalne, posortowane, poprawne adresy email
#Przykład:
#python clean_email.py emails.txt cleaned_emails.txt

import sys

try:
    f_in_path = sys.argv[1]                         #przez cmd pierwszy argument to nazwa pliku z którego bierzemy emaile
    out_f_path = sys.argv[2]                        #przez cmd drugi argument to nazwa pliku do którego wrzucamy emaile
except IndexError:
    f_in_path = "emails.txt"
    out_f_path = "cleaned_emails.txt"


emails = set()                                      #mails jest zbiorem
with open(f_in_path) as f:
    for i in f:
        i = i.strip().lower()                 #strip usuwa puste znaki przed i po stringu, lower szuka stringów z małej litery
        if i.count("@") == 1:                    #jeśli w linii jest tylko jeden znak @
            emails.add(i)                        #to dodaj tą linię do zbioru emails

#sprawdzamy jaki zbór nam się pojawił
print(emails)                                       #{'user-6@email.com', 'user-4@email.com', 'user-2@email.com', 'user-5@email.com', 'user-3@email.com', 'user-1@email.com', 'user-0@email.com', 'user-9@email.com', 'user-8@email.com', 'user-7@email.com'}

with open(out_f_path, "w") as f:
    for i in sorted(emails):
        f.write(i + "\n")

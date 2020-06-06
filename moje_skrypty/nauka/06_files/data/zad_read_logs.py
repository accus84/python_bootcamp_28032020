import sys

try:
    f_path = sys.argv[1]            #będzie wczytywany dodatkowy argument z terminala
                                    #czyli teraz wchodzimy w terminal, podajemy w nim scieżkę jako pioerwszy parametr oraz nazwę pliku logs.txt jako drugi parametr i tak uruichamiamy
except IndexError:                    #czyli w terminalu pythona wpisujemy: C:\Users\azolynski\Desktop\ALX_szkolenie\workspace\moje_skrypty\06_files\data>zad_read_logs.py logs.txt
    f_path = "logs.txt"  #to jest ten argument, dzięki temu zamiast całej ścieżki możemy dalej podawać f_path

#Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
# Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie przebywania każdego użytkownika w systemie

last_login = {}
user_total_time = {}

with open(f_path, "r") as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action =="LOGIN":
            last_login[login] = time                #kluczem jest login, wartością klucza jest time
        elif action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login, 0) + time - last_login[login]
print(user_total_time)          #czas który juser spedzil w systemie

print("Czas przebywania w systemie: ")
for user, time in sorted(user_total_time.items(), key = lambda x: x[1], reverse = True):        #sorted sortuje listę od najmniejszej do największej
    print(f" - {user:>2}, {time}")          #po - dalsza część będzie oddzielona o 2 miejsca

#pomoc w sorted
x = ["a3", "c4", "b1"]
print(sorted(x))                            #['a3', 'b1', 'c4']  sortowanie po piuerwszej literze
print(sorted(x, key = lambda x: x[1]))      #['b1', 'a3', 'c4']  sortowanie po drugiej literze

f.close()

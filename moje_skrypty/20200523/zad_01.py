#napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii.
#Obsłuż sytuację gdy user nie poda nazwy pliku lub poda błędną nazwę

#najpepiej stosować with open, wtedy nie trzeba podawać exception
with open ("nowy_plik.txt", "w") as f:
    f.write("To jest pierwszy wiersz.\nTo jest drugi wiersz.\nA to jest trzeci wiersz.")
    f.close()

with open("nowy_plik.txt", "r") as f:
    count = 1
    for line in f.readlines():
        print(f"{count}: {line}")
        count+=1
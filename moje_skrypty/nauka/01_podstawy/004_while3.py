#zapytać o 7 temperatur, policzyć średnią
day = 1
temp_total = 0                  #tworzymy zmienną temp_total o wartości 0, w której będą sumowane temperatury
while day < 8:
    temp = int(input(f"Podaj temperaturę dla {day} dnia: "))
    day += 1
    temp_total += temp
print(f"Średnia temperatur dla 7 dni wynosi {round((temp_total / 7), 2)}")

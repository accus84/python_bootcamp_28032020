#zapytać o 7 temperatur, policzyć średnią
day = 1
temp_total = 0
while day < 8:
    temp = int(input(f"Podaj temperaturę dla {day} dnia: "))
    print(temp)
    day +=1
    temp_total += temp
print(f"Średnia temperatur dla 7 dni wynosi {round((temp_total / 7), 2)}")


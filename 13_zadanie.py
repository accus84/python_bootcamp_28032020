#zapytać o 7 temperatur, policzyć średnią
day = 1
temp_total = 0
while day < 8:
    temp = int(input(f"Podaj temperaturę dla {day} dnia: "))
    print(temp)
    day +=1
    temp_total += temp
print(f"Suma temperatur 7 dni wynosi {int(temp_total / 7)}")


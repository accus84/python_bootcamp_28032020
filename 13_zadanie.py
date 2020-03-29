#zapytać o 7 temperatur, policzyć średnią
dni = 1
temp_total = 0
while dni < 8:
    temp = int(input(f"Podaj temperaturę dla {dni} dnia: "))
    print(temp)
    dni +=1
    temp_total += temp
print(f"Suma temperatur 7 dni wynosi {int(temp_total / 7)}")


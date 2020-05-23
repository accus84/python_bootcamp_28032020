# metoda capitalize() powoduje wypisywanie nazwy od dużej litery
# metoda lower() powoduje wypisywanie całej nazwy z małych liter
curr_year = 2020

first_name = input("Imię: ")
last_name = input("Nazwisko: ")
b_year = int(input("Rok urodzenia: "))
profession = input("Zawód: ")

age = curr_year - b_year
print(age)
result = f"""
imie i nazwisko: {first_name.capitalize()} {last_name.capitalize()}
=============================
rok urodzenia:      {b_year}
zawód:              {profession.lower()}
"""

print(result)


import re

words = ("zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć")
char = list(input("Wprowadź liczbę: "))

only_digits = list([i for i in char if i.isnumeric()])

for i in only_digits:
    i = int(i)
    print(words[i], end = " ")
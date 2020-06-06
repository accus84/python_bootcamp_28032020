import re                          #regular expression
#są też narzędzia jak regexp online gdzie można ćwiczyć wyrażenia
#super strona regex101.com


napis = "522-30312-345 123-34312-345 123-312-345"
kod_pocztowy_pattern = re.compile("\d{2}-\d{3}")
data_pattern = re.compile("\d{2} \w{3} \d{4}")
email_pattern = re.compile("[\w\.\-]+@(\w+\.)+w")

pesel_pattern = re.compile("\d{11}")    #patern ma mieć dokładnie 11 cyfr
print(pesel_pattern.match(napis))       #<_sre.SRE_Match object; span=(0, 11), match='55215359111'> - napis pasuje bo jest match

kod_pocztowy = "12-334"
kod_pattern = re.compile("\d{2}-\d{3}") #2 cyfry, -, 3 cyfry
print(kod_pattern.match(kod_pocztowy))  #<_sre.SRE_Match object; span=(0, 6), match='12-334'>   pasuje

#oznaczenia:
jedna_liczba = re.compile("\d")
print(jedna_liczba.match(napis))        #znajduje jedną liczbę 5

dwie_liczby = re.compile("\d\d")
print(dwie_liczby.match(napis))        #znajduje dwie liczby 55


#pattern na kod pocztowy
#^\d{2}-\d{3}$| \d{2}-\d{3}$ \d{2}-\d{3}...





#ukryte są daty
#kody pocztowe
#adresy
#zadanie:
#wybrać to co jest nam potrzebne z input.txt

#jak?
#użyć wyrże regularnych

import re

napis = "522-30312-345 123-34312-345 123-312-345"
kod_pocztowy_pattern = re.compile("\d{2}-\d{3}")
data_pattern = re.compile("\d{2} \w{3} \d{4}")          #2 cyfry, 3 litery, 4cyfry
email_pattern = re.compile("[\w+\.\-]+@+[\w+\.]+\w+")
with open("input.txt") as f:
    text = f.read()

#kody pocztowe
print(kod_pocztowy_pattern.findall(text))       #['59-996', '58-950', '30-666', '14-113', '84-979', '75-254'... z tekstu pojawiają się wszystkie patterny na kod pocztowy
#daty
print(data_pattern.findall(text))               #['21 May 1995', '24 Oct 2003', '15 Jun 1991', '02 Sep 2008', 09 Feb 1990'...
#adresy
print(email_pattern.findall(text))




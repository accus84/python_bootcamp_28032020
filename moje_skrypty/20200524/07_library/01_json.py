#json to format tekstowy do przesyłania danych gdzie dokumenty są zbudowane według pewnych reguł
#to jest bardzo przydatne bo wiele danych udostępnianych jest w formie jsona
#są narzędzia na necie (dużo) które srawdzają czy składnia naszego jsona jest ok
#żeby skorzystać z jsona musimy zaimportować moduł json

import json
#json oferujem 4 metody:
#load - odczyt danych z pliku (deserializacja)
# dump - zapisywanie do pliku (serializacja)
# loads - odczyt danych z tekstu
# dumps - serializacja do tekstu

#loads
#napis zawierający jsona
text = '{"a":2, "b": 4}'

#zaladuj napis (string)
dane = json.loads(text)             #odczyt stringa text z
print(dane)                         #{'a': 2, 'b': 4}
print(type(dane))                   #<class 'dict'>

#dumps
x = {i: i*3 for i in range(10)}
print(x, type(x))                   #{0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27} <class 'dict'>

#wypintuje jak będzie wyglądał dump
print(json.dumps(x))                #{"0": 0, "1": 3, "2": 6, "3": 9, "4": 12, "5": 15, "6": 18, "7": 21, "8": 24, "9": 27}

#load
with open("dane.json") as fp:       #pobranie danych z pliku dane.json
    dane = json.load(fp)
    print(dane)

#dump - utworzenie nowego pliku obok dane.json
x = [1, 10, 11, 12, 14]
with open("dane2.json", "w") as fp: #został utworzony plik
    json.dump(x, fp)
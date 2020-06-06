import json

"""
load - odczytywanie danych z PLIKU (deserializacja)
dump - zapisywanie danych do PLIKU (serializacja)
loads - odczyt danych z TEKSTU
dumps - serializacja do TEKSTU
"""

# load  - odczyt z pliku
with open("dane.json") as fp:
    dane = json.load(fp)
print(dane)                                     #[{'imie': 'RafaĹ‚', 'wiek': 40}, {'imie': 'Adam', 'wiek': 42}]

# loads - odczyt z tekstu
text = '{"a":2, "b":4}'
dane = json.loads(text)
print(dane)                                     #{'a': 2, 'b': 4}
print(type(dane))                               #<class 'dict'>     dane są typu słownik

# dump - zapis do pliku
x = [1, 10, 11, 12, 14]
with open("dane2.json", "w") as fp:
    json.dump(x, fp)                            #w pliku dane2.json jest [1, 10, 11, 12, 14]

# dumps - "zapis" do tekstu
x = {i: i*3 for i in range(10)}
print(x, type(x))
print(json.dumps(x))                            #{"0": 0, "1": 3, "2": 6, "3": 9, "4": 12, "5": 15, "6": 18, "7": 21, "8": 24, "9": 27}






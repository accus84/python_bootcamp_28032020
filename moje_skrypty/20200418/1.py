# słwoniki
pol_ang = dict()
pol_ang["pies"] = "dog"
print(pol_ang)

pol_ang = {
    "kot": "cat",
    "ptak": "bird"
}
print(pol_ang)

#inny sposób tworzenia
dict_2 = dict(a = 10, b = 22, c = 33)       #a b c to zmienne, które mają swoje prawa
print(dict_2)

#inny sposób tworzenia
dict_3 = dict([
    ["x", "ala"],
    ["y", "kot"]
])
print(dict_3)

print(dict_3.keys()) #wypisuje klucze
print(dict_3.values())   #wypisuje wartości
print(dict_3.get("x"))      #pobiera wartość klucza x
print(dict_3["x"])

if 'z' in dict_3:       #czy jest klucz z
    print(dict_3["z"])
else:
    print("brak")

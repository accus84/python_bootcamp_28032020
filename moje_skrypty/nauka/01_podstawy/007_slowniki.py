# pol_ang = dict()
#słownik ma klucz i wartość klucza
pol_ang = {
    "kot": "cat",
    "ptak": "bird"
}

print(pol_ang)                          #{'kot': 'cat', 'ptak': 'bird'}

pol_ang["kot"] = "kitty"                #zmiana klucza "kot" z "cat" na "kitty"
pol_ang["pies"] = "dog"                 #dodanie klucza i jego wartości

print(pol_ang)                          #{'kot': 'kitty', 'ptak': 'bird', 'pies': 'dog'}

dict_2 = dict(a=10, b=22, c=33)
print(dict_2)                           #{'a': 10, 'b': 22, 'c': 33}

dict_3 = dict([
    ["x", "ala"],
    ["y", "kot"]
])

print(dict_3)                           #{'x': 'ala', 'y': 'kot'}

print(dir(dict_3))                      #jakie metody ma słownik dict_3

print()

print(dict_3.keys())                    #dict_keys(['x', 'y'])                      - wypisanie kluczy słownika
print(dict_3.values())                  #dict_values(['ala', 'kot'])                - wypisanie wartości kluczy słownika
print(dict_3.items())                   #dict_items([('x', 'ala'), ('y', 'kot')])   - wypisanie wszystkich itemów słownika

print(dict_3.get("x"))                  #wypisanie wartości dla klucza "x"
print(dict_3.get("z", "brak"))          #wypisanie włownika dla klucza "z", a w przypadku braku tego klucza wypisanie "brak"

if 'z' in dict_3:                       #wypisanie słownika dla klucza "z", a w przypadku braku tego klucza wypisanie "brak" - to samo co powyżej ale za pomocą pętli
    print(dict_3["z"])                  #nie ma z w słowniku dict_3
else:
    print("brak")                       #brak

#cwiczenie
nba = {'Lebron James': 'LAL', 'James Harden': 'HOU', 'Kevin Durant': 'BKN'  }
#wypisanie slownika
print(nba)                              #{'Lebron James': 'LAL', 'James Harden': 'HOU', 'Kevin Durant': 'BKN'}
#wypisanie kluczy
print(nba.keys())                       #dict_keys(['Lebron James', 'James Harden', 'Kevin Durant'])
#wypisanie wartości
print(nba.values())                     #dict_values(['LAL', 'HOU', 'BKN'])
#wypisanie itemów
print(nba.items())                      #dict_items([('Lebron James', 'LAL'), ('James Harden', 'HOU'), ('Kevin Durant', 'BKN')])

#wypisanie wartości dla danego klucza
print(nba.get('Lebron James'))          #LAL (jeśli nie będzie podanego klucza to pojawi się None)
#wypisanie wartości dla danego klucza i zastpienie None słowem 'nie ma' jeśli nie znaleziono klucza
print(nba.get('Horace Grant', 'nie ma'))#nie ma

#wypisanie values po pętli
for keys, values in nba.items():
    print(keys, end =' ')               #Lebron James James Harden Kevin Durant




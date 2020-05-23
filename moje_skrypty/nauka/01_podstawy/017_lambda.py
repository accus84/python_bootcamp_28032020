x = list(range(1, 11))
print(x)
#jak zrobic z tego szesciany czyli do potęgi3
szesciany = []
for e in x:
    szesciany.append(e **3)
print(szesciany)

#lepiej
x = list(range(1, 11))
print([e **3 for e in x])       #jeślik chcemy zapisać za pomocą minifunkcji to trzeba pamiętać żeby całość dać w [] w przypadku listy

#teraz szesciany ale tylko parzyste
x = list(range(1, 11))
print([e **3 for e in x if e % 2 == 0])
#można to zastosować do zbioru, wynik taki sam ale nieuporządkowany
x = list(range(1, 11))
print({e **3 for e in x if e % 2 == 0})
#słownik
x = list(range(1, 11))
print({e: e **3 for e in x if e % 2 == 0})
#tupla, można zrobić przez rzutowanie
x = list(range(1, 11))
print(tuple(e **3 for e in x if e % 2 == 0))

#utworzyć listę zawierającą liczbę zmiennoprzecinkową od 0.0 do 1.0 z krokiem 0.1 (range)
print([x/10 for x in range(11)])

#zbiór tupli zawierających 3 elementy - liczbę, jej kwadrat i sześcian w przedziale od -10 do 10
print({(x, x**2, x**3) for x in range(-10, 11)})

#słownik mapujący napisy na ich długość powstały ze zbioru napisów
napisy = {"xxx", "yyyy", "xx", "xxxxxcccfv"}
print({napis: len(napis) for napis in napisy})

l = list(range(1,11))
print(l)
#dla listy
print([i for i in l])               # całość w []
#dla zbioru
print({i for i in l})               # całość w {}
#dla słownika
print({i: i for i in l})            # dodatkowo klucz, po kluczu jak wcześniej, całość w {}


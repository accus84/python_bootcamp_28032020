produkty = {
    "ziemniaki": 2.25,
    "pomiodory": 4.15,
    "cebula": 1.99,
    "kalafior": 3.20
}

print(produkty.get("ziemniaki"))    # wypisuje wartość danego słownika, jeśli nie ma takiego słownika to wpisywana jest wartość None
print(produkty.values())            # wypisuje same wartości
print(produkty.keys())            # wypisuje same słowniki

#Napisz program zliczaqjący liczbę wystąpień każdego znaku w podanym przez użytkownika napisie
#jak użytkownik poda ekst dzień dobry to w tym tekscie są znaki
#kluczem będzie znak a wartością będzie ilość, ile razy ten znak występue w tekście

zliczenia = dict()
napis = input("Podaj jakiś napis: ")
for i in napis:
    zliczenia[i] = napis.count(i)
print(zliczenia)

#drugie rozwiazanie
zliczenia = dict()
for znak in napis:
    if znak in zliczenia:     #sprawdza czy w słowniku zliczenia występuje klucz znak
        zliczenia[znak] = zliczenia[znak] +1
    else:
        zliczenia[znak] = 1
print(zliczenia)

#inne rozwiązanie
zliczenia = dict()
for znak in napis:
    zliczenia[znak] = zliczenia.get(znak, 0) +1     #0 jest po to żeby defaultowo zamiast None było ustawione 0 jeśli nie ma tego klucza
print(zliczenia)
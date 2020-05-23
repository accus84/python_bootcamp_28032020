#Utworzyć listę z sześcianami. Lista ma się składać z cyfr parzystych od 0 do 10

x = list(range(1, 11))
print(x)                                                #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

szesciany = []
for i in x:
    if i % 2 == 0:
        szesciany.append(i ** 3)
print(szesciany)                                        #[8, 64, 216, 512, 1000]

#utworzyć listę liczb od -10 do 10 i ich sześcianami
print([[i, i**3] for i in range(-10, 11)])              #print i oraz sześcianu i w pętli od -10 do 10

#utworzyć listę liczb od 0 do 100 z jej kwadratami i sześcianami
print([[i, i**2, i**3] for i in range(0,100)])

#poniżej jest zbiór zatem jest nieuporządkowany
print({i**3 for i in x if i % 2 == 0})                   #dla 2, 4, 6, 8, 10 sześciany to {512, 64, 8, 1000, 216} (nieuporządkowane)

#poniżej są słowniki
print({i: i ** 3 for i in x if i % 2 == 0})             #{2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}

#poniżej tuple
print(tuple(el ** 3 for el in x if el % 2 == 0))        #(8, 64, 216, 512, 1000)

print()
print()

#zadania
#wypisać zakres od 0.0 do 1.0
#wiedząc że x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], skorzystajmy z tego, że 0.1, 0.2, 0.3 itd można przedstawić jako x/10
print([x/10 for x in range(11)])

print()
#utworzyć zbiór słowników z kluczem ze zbioru napisy i wartością o długości każdego z elementów zbioru napisy
napisy = {"xxx", "yyyyy", "xx", "xxxxxxxxxcxcxcxcxcx"}
#print({klucz:wartość})
#a to każdy element ze zbioru napisy o czym świadczy zapis for a in napisy
#len(a) to ługość każdego elementu ze zbioru napisy
print({a:len(a) for a in napisy})                       #{'xxx': 3, 'xx': 2, 'xxxxxxxxxcxcxcxcxcx': 19, 'yyyyy': 5}

#Utworzyć listę z sześcianami. Lista ma się składać z cyfr parzystych od 0 do 10
print()
x = list(range(1,11))
print(x)

szesciany = []
for i in x:
    if i % 2 ==0:
        i = i ** 3
        szesciany.append(i)
print(szesciany)                                        #[8, 64, 216, 512, 1000]

#to samo za pomocą minifunkcji
#tuple      - w princie trzeba wypisać że to jest tuple
print(tuple(i**3 for i in x if i % 2 == 0 ))            #(8, 64, 216, 512, 1000)
#lista      - wypisanie  dodatkowo z cyfrą podniesioną do sześcianu  - w princie musi być  wszystko spięte [] bo to jest lista
print([[i, i**3] for i in x if i % 2  ==0 ])            #[[1, 1], [2, 8], [3, 27], [4, 64], [5, 125], [6, 216], [7, 343], [8, 512], [9, 729], [10, 1000]]
#zbiór      - czyli w princie musi być  wszystko spięte {}o to jest zbiór
print({i**3 for i in x if i % 2 == 0})                  #{512, 64, 8, 1000, 216}
#słownik    - i i sześcian i - pamiętać, żę tu też wszystko musi być ołożone {}
print({i : i**3 for i in x if i % 2 ==0})               #{2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}

#ze zbioru marka zrobić cłownik gdzie wartością będzie długość każdego z elementów zbioru
marka = {"opel", "fiat", "renaul", "lamborghini", "ferrari", "konig"}
print({i : len(i) for i in marka})

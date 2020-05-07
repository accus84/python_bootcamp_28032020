#krotka (tupla)
x = tuple()
x = (1, 2, "ala", 2.0, "ma kota", 2)
print(x)
print(type(x))                  #jakiego rypu jest x
print(dir(x))                   #jakie metody operują na x
print(x.index("ala"))           #na którym miejscu jest element "ala"
print(len(x))                   #długość tupli
print(len("ala"))               #długość elementu ala w tupli
print(x.count(2))               #zlicz ile jest "2" w tupli
print(3 in x)                   #czy jest 3 w tupli     False
print(x[0:3])                   #podaj elementt od 0 do 3:  1,2,"ala"

if 'ma kota' in x:              #jeśli 'ma kota' jest w tupli x
    print(x.index('ma kota'))   #to wypisz którym elementem tupli jest ',a kota' - 4

print("b" in "Ola")             #pokazuje True jesli jest albo False jeśli nie ma 'b' w 'Ola'
print(2 in x)                   #pokazuje True jesli jest albo False jeśli nie ma 2 w x
print(len("Ala"))               #długość słowa Ala

#Stwórz tuplę zawierającą 10 różnych liczb całkowitych i podaj
#drugi element
#przedostatni element
#elementy od 3 do 7 włącznie
#co trzeci element
#co drugi element od końca

tupla = (1, 13, 5, 66, 4, 9, 10, 8, 11, 100)

print(f"""
Drugi element: {tupla[1]}
Przedostatni element: {tupla[-2]}
Elementy od 3 do 7: {tupla[2:7]}
Co trzeci element: {tupla[::3]}                     ## ::3 to co trzeci element
Co drugi element licząc od końca: {tupla[::-2]}
""")

#dodawanie tupli
x = (1, 2)
y = (3, 4)
print(x + y)                    #(1, 2, 3, 4)

#zamiana wartośći 2 zmiennych
a, b = 1, 3
print(a, b)                     #1 3
a, b = b, a
print(a, b)                     #3 1

wynik = (a, b) == (1, 3)        #True jeśli prawdziwe
print(wynik)                    #a więc wyjdzie False
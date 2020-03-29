#Stwórz tuplę zawierającą 10 różnych liczb całkowitych i podaj
#drugi element
#przedostatni element
#elementy od 3 do 7 włącznie
#co trzeci element
#co drugi element od końca

tupla = (1, 13, 5, 66, 4, 9, 10, 8, 11, 100)
print(f"Drugi element: {tupla[1]}")
print(f"Przedostatni element: {tupla[-2]}")
print(f"Elementy od 3 do 7: {tupla[2:7]}")
print(f"Co drugi element licząc od końca: {tupla[::3]}")
print(f"Co drugi element licząc od końca: {tupla[::-2]}")
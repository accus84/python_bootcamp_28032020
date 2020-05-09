#zad 3
lista = [-5, 0, 12, 5, 16, 6, 4, -3]

def sortowanie(l):
    for i in range(len(l)):
        for k in range(i + 1, len(l)):
            if l[k] < l[i]:
                l[k], l[i] = l[i], l[k]
    return l

print(sortowanie(lista))
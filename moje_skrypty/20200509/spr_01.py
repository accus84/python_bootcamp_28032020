#zad 3
lista = [-5, 0, 12, 5, 16, 6, 4, -3]

def sortowanie(l):
    for i in range(len(l)):
        for k in range(i + 1, len(l)):
            if l[k] < l[i]:
                l[k], l[i] = l[i], l[k]
    return l

print(sortowanie(lista))

#zad4
zrodla = {"a": 10, "b":30}
print(zrodla.get("c", "brak"))

print()

#zad5
def foo(*args, **kwargs):
    print(f"pozycyjnych: {len(args)}")
    print(f"kluczowych: {len(kwargs.items())}")


foo(2,4,5, a=1, b=4)
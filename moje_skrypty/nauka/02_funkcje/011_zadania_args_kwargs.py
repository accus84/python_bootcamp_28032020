#args - nieokreślona liczba argumentów
def myFun(*args):                   #args jest tuplą
    for i in args:                  #przechodzenie po elementach tupli
        print (i)

myFun("Hello", "Welcome", "Hi")
#Hello
#Welcome
#Hi

#to samo można osiągnąć przez zapis
def myFun(*args):  # args jest tuplą
    print(args)

myFun("Hello", "Welcome", "Hi")
#('Hello', 'Welcome', 'Hi')

#możemy także jawnie podawać w funkcji argumenty:
def myFun(*args, z=15):             #args jest tuplą
    for i in args:                  #przechodzenie po elementach tupli
        print (i)
    print(z)

myFun("Hello", "Welcome", "Hi")
#Hello
#Welcome
#Hi
#15

#kwargs zawiera parę nazwa-wartość argumentu, artgumenty są dostępne w postaci słownika *słowniki mają funkcję items() po której można wyszukiwać)
#kwargs używamy gdy do funkcji chcemy przekazać argumenty, które wyróżniają się nazwą
def parametr_kwargs(**kwargs):
    print(kwargs)

parametr_kwargs(a=48, b=111, c=12)
#{'a': 48, 'b': 111, 'c': 12}

#w przypadku kwargs również możemy podawać jakieś argumenty
def parametr_kwargs(a=6, **kwargs):
    print(a)
    print(kwargs)       #b i c nie zostały zdefiniowane w funkcji więc trafiły jako kwargs

parametr_kwargs(a=48, b=111, c=12)
#48                     a miało wartość domyślną 6 ale zmieniliśmy jej na 48 stąd taki wynik
#{'b': 111, 'c': 12}    #reszta argumentów, a już wystąpiło więc jest pomijane

def param_kwargs(**kwargs):
    for x, y in kwargs.items():
        print(len(kwargs))          #liczba parametrów
        print(x, y)

param_kwargs(a=10, b=20, c=30)

#KLASYCZNY PRZYKLAD ARGS I KWARGS
#zamiana definicji w słowniku jeśli pojawi się wystąpienie tego słowa w args
def f(*args, **kwargs):
    zwierzeta = " ".join(args)
    for x, y in kwargs.items():
        zwierzeta = zwierzeta.replace(x, y)
    return (zwierzeta)

print(f("sowa", "królik", "kot", "pająk"))
#sowa królik kot pająk
print(f("sowa", "królik", "kot", "pająk", sowa= "ptak"))
#ptak królik kot pająk

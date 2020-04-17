# wyrażenie lambda to mała anonimowa funkcja
# może pobrać dowolną liczbę argumentów ale ma tylko jedno wyrażenie
# lambda <argumenty> : jak mają na siebie oddziaływać
x = lambda a : a + 10       # inaczej mówiąc x to a zwiększone o 10
print(x(5))
# lambda może przyjąć dowolną liczbę argumentów
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# po co używać wyrażeń lambda
# przydaje się w funkcjach gdzie np. argument w funkcji musi być powielony n razy
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
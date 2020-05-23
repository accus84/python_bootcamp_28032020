zbior = set()               #utwórzenie pustego zbioru
zbior.add("x")              #dodanie "x" do zbioru
zbior.add(1)                #dodanie 1 do zbioru
print(zbior)                #{1, 'x'}               - zbiory są nieuporządkowane

for el in zbior:            #{1, 'x'}               - to samo co powyżej ale za pomocą pętli
    print(el)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}

print(a | b)                #{1, 2, 3, 4, 5}        - sumowanie zbiorów
print(a & b)                #{2, 3, 4}              - iloczyn (część wspólna zbiorów)
print(a - b)                #{1}                    - odejmowanie 1,2,3,4 - 2,3,4,5 co zostaje w zbiorze a
print(b - a)                #{1}                    - odejmowanie 2,3,4,5 - 1,2,3,4 co zostaje w zbiorze b
print(a ^ b)                #{1, 5}                 - różnica symetryczna (co jest tylko w a i b)

print(a.pop())              #1                      - pop usuwa pierwszy element ze zbioru a, czyli usuwa 1
print(a)                    #{2, 3, 4}              - ...co widać po wyprintowaniu tego zbioru

lista = list(range(100))    #jak szybko zrobić listę od 0 do 100
print(lista)
zbior = set(range(100))     #jak szybko zrobić zbior od 0 do 100
print(zbior)


elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
elementy2 = {"aaa", "aba", "ccc"}
elementy = set(elementy)
print(f" Unikalne zbiory: {elementy ^ elementy2}, liczba unikalnych zbiorów: {len(elementy ^ elementy2)}")
print(f" Część wspólna zbiorów: {elementy & elementy2}, liczba wspólnych zbiorów: {len(elementy & elementy2)}")


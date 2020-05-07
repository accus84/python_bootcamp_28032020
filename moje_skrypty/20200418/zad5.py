elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]
elementy2 = {"aaa", "aba", "ccc"}
elementy = set(elementy)
print(f" Unikalne zbiory: {elementy ^ elementy2}, liczba unikalnych zbiorów: {len(elementy ^ elementy2)}")
print(f" Część wspólna zbiorów: {elementy & elementy2}, liczba wspólnych zbiorów: {len(elementy & elementy2)}")

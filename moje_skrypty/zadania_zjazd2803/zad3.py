# Napisz program, który wczyta od użytkownika liczbę X, a następnie wyświetli "kwadrat" z gwiazdek o długości boku X

num = int(input("Podaj jakąś liczbę X: "))
square = num*"*"
print(square)
i = 1
for i in range(0, num-2):
    print(square[0] + (num - 2)*" " + square[-1])
print(square)


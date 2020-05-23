#x = input("Wprowadz cyfre")
#print(X)

try:
    x = input("Wprowadz cyfre: ")
except NameError as e:
    print("Wyjasnienie", e)
print("Cos dalej")

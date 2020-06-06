# Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo odlewej, jak i od prawej).

text = "Łapał za kran, a kanarka złapał"

#funkcja odwracająca string
def reverse(x):
    x = x.lower()
    x = x.replace(" ", "")
    y = list()
    for i in x:
        if i.isalpha() == True:
            y.append(i)
    return y[::-1]

def czy_palindrom(a):
    a = a.lower()
    a = a.replace(" ", "")
    y = list()
    for i in a:
        if i.isalpha() == True:
            y.append(i)
    if y == reverse(a):
        return True
    return False

print(czy_palindrom(text))

def test_czy_palindron():
    assert czy_palindrom("kajak") == True
    assert czy_palindrom("Łapał za kran, a kanarka złapał") == True
    assert czy_palindrom("python") == False

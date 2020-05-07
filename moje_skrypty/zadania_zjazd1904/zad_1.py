# Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo odlewej, jak i od prawej).

text = "kajak"

#funkcja odwracająca string
def reverse(x):
    return x[::-1]

def czy_palindrom(a):
    if a == reverse(a):
        return True
    return False

print(czy_palindrom(text))

def test_czy_palindron():
    assert czy_palindrom("kajak") == True
    assert czy_palindrom("python") == False


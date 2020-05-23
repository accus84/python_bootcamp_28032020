#rekurencja
#def decrement(n):
#    if n == 0:          #zabezpieczenie przed wieczną rekurencją, break nie ma tu zastosowania bo on działa w pętli
#        print(0)        #...
#        return          #teraz funkcja się zakończy
#    print(n)            #to już jest inna funkcja
#    decrement(n-1)

# decrement(10)

#tworzenie silni za pomocą rekurencji

def silnia(n):
    if n<0:
        return "Error"
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)

print(silnia(4))

#def test_silnia():
#    assert silnia(0) == 0
#    assert silnia(1) == 1
#    assert silnia(2) == 2
#    assert silnia(3) == 6
#    assert silnia(5) == 120
#    assert silnia(-5) == "Error"

text = "ala ma kota"
def reku_print(text):
    dlugosc = len(text)  # 11
    #reku_print(text[dlugosc - 1])
    #nie można użyć pętli
    #print(text[dlugosc - 1])
    #print(text[dlugosc - 2])
    #print(text[dlugosc - 3])
    return reku_print(text) -1
print(reku_print(text))

        #return reku_print(text[len(text) -1])



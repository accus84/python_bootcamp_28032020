
# Napisz funkcję obliczającą liczbę znaków w zadanym napisie (TYLKO) pomiędzy zadanymi znakami.
# Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi - odpowiednio < i >.
# Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.

def policz_znaki(text, start = "<", stop = ">"):        #domyślne wartości to start jako < i stop jako >
    poziom = 0
    licznik = 0
    for i in text:                                      #dla każdego naku w tekście
        if i == start:                                  #jeśli znakiem jest '<'
            poziom += 1                                 #dodaje do poziomu +1 aż napotkam znak stop
            continue                                    #continue oznacza że jak natkieniemy się znowu na znak '<' to i tak będzie dalsze zliczanie
        elif i == stop:                                 #a kiedy już napotkam znak stop
            poziom -= 1                                 #to odejmuje od poziomu wartość -1
            continue
        licznik += poziom                               #po każdym obrocie zliczany jet licznik przez dodawanie kolejno poziomu
    return licznik

print(policz_znaki("<cos>"))                            #3
print(policz_znaki("jakies <znaczki>"))                 #7
print(policz_znaki("a <a<a<a>>>"))                      #6

def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko>ta a kot ma ale') == 2
    assert policz_znaki('ala ma <kota> a <kot> ma ale') == 7
    assert policz_znaki('ala ma [kota] a [kot] ma ale', "[", "]") == 7
    assert policz_znaki('a <a<a<a>>>') == 6


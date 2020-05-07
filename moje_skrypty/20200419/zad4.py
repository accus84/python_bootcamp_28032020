#Zaimplementuj funkcję formatującą podane napisy.
#Przykład użycia:
#>>> formatuj('koszt $cena PLN','kwota $cena brutto',cena=10 )
#'koszt 10 PLN\nkwota 10 brutto'

def formatuj(*teksty, **znaczniki):
    text = "n".joint(teksty)
    for znacznik, wartosc in znaczniki.items():
        text = text.replace("$"+znacznik, str(wartosc))
    return text

formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10 )

def test_formatuj():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10 ) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto') == 'koszt $cena PLN\nkwota $cena brutto'

#*args są bez równa się
#kwargs są tam gdzie cena=10


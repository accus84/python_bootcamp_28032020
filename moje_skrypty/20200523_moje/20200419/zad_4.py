# Zaimplementuj funkcję zliczającą liczbę wystąpień poszczególnych słów w zadanym napisie.
text = 'ala ma kota i kot ma ala'

#sposób 1
def policz_slowa(x):
    zliczenia = dict()
    for i in x.split(" "):
        if i in zliczenia:
            zliczenia[i] = zliczenia[i] + 1     #jeśli klucz istnieje w słowniku, jego wartość zwiększa się o 1
        else:
            zliczenia[i] = 1                    #jeśli klucz jeszcze nie istnieje w słowniku, jego wartość początkowa to 1
    return zliczenia

print(policz_slowa(text))                       ##{'ala': 2, 'ma': 2, 'kota': 1, 'i': 1, 'kot': 1}

#sposób 2
def policz_slowa2(x):
    zliczenia = dict()
    for i in x.split(" "):
        zliczenia[i] = zliczenia.get(i, 0) + 1  #jeśli klucz nie istnieje to wartością początkową jest 0 + 1, jeśli istnieje to dodawane jest 1
    return zliczenia

print(policz_slowa2(text))                      #{'ala': 2, 'ma': 2, 'kota': 1, 'i': 1, 'kot': 1}

def test_policz_slowa():
    assert policz_slowa('ala ma kota i kot ma ala') == {'ala': 2, 'ma': 2, 'kota': 1, 'i': 1, 'kot': 1}
    assert policz_slowa('cos jest nie tak') == {'cos': 1, 'jest': 1, 'nie': 1, 'tak': 1}

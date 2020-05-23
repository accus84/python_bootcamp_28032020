for x in "abc":
    if x == 'b':
        break                               #break wychodzi z pętli jak natrafi na warunek, b już nie będzie uwzględnione
    print(x)                                #a

print()

for x in "abc":
    if x == 'b':
        continue                            #continue pomija warunek i wykonuje się dalej czyli pomija b
    print(x)                                #a c

print()

for y in "123":
    for x in "abc":                         #powinno być a1 a2 a3, b1 b2 b3, c1 c2 c3
        if x == "b":
            break                           #wyjśćie ALE TYLKO Z PĘTLI ZAGNIEŻDŻONEJ, czyli for x in "abc" zwraca tylko wartość a
        print(x + y)                        #a1 a2 a3



#moje ćwiczenia

text = "Lebron James Junior"
for i in text:
    if i =='u':
        break
    print(i, end = '')                      #Lebron James

print()

for i in text:
    if i =='J':
        continue
    print(i, end ='')                       #Lebron ames unior
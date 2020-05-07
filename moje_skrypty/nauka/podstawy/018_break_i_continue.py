#INSTRUKJCE BREAK I CONTINUE SĄ STOSOWANE W PĘTLACH FOR I WHILE

#instrukcja break jest używana do zakończenia działania pętli
#instrukcja continue jest używana do pominięcia warunku w pętli

#break w pętli for
text = "abrakadabra"
for i in text:
    if i == "d":                #jeśli natrafimy na literę 'd' to przerywamy działanie pętli
        break
    print(i, end = '')          #abraka     wyświetlany wynik aż do przerwania

print()

#break w pętli while
x = 0
while x < 5:
    print(x, end = '')          #0123   wzięło też 3 dlatego, że najpierw wyświetlane jest x a dopieró poźniej jest przerwanie jeśli x==3
    x += 1
    if x == 3:
        break

print()

#instrukcja continue pozwala na opuszcenie wykonywania dalszej części skryptu po tej instrukcji i powrócenie do początku pętli

#continue w pętli for
text = "abrakadabra"

for i in text:
    if i == "a":                #jeśli natrafimy na literę 'a' to pomijamy dalszą część skryptu i pobieramy kolejny element zmiennej tekstowej
        continue
    print(i, end = '')          #brkdbr

print()

#continue w pętli while
x = 0
while x < 5:
    x +=1                       #w porównaniu do break tutaj inkrementacja i print są zamienione kolejnością
    if x == 3:
        continue
    print(x, end = '')          #1245

#PETLA FOR WYGLADA IDENTYCZNIE DLA BREAK I CONTINUE

#for i in text:
#    if i == "a":
#        break/continue
#    print(i, end = '')

#PETLA WHILE

#x = 0
#while x < 5:
#    print(x, end = '')          #0123   wzięło też 3 dlatego, że najpierw wyświetlane jest x a dopieró poźniej jest przerwanie jeśli x==3
#    if x == 3:
#        break
#    x += 1

#x = 0
#while x < 5:
#    x +=1                       #w porównaniu do break tutaj inkrementacja i print są zamienione kolejnością
#    if x == 3:
#        continue
#    print(x, end = '')          #1245
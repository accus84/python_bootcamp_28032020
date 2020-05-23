x = 10
#przykład 1
while x > 0:                    #tak długo aż x > 0 to rób
    print(x, end = '')          #10987654321
    x -= 1                      #odejmowanie 1 od wartośći x

print()

#przykład z pętlą break - jest bardzo podobna do standardowej tylko na końcu dajemy warunek przerwania
x = 10
while True:                     #tak długo aż jest True
    print(x, end = '')          #10987654321
    x -= 1                      #po wyprintowaniu zmniejsz o 1
    if x == 0:                  #a kiedy osiągnie 0
        break                   #.. to break - oznacza przerwanie programu po spełnieniu warunku i == 0

print()

#w continue najpierw dajemy warunek a dopiero później inkrementujemy
#przykład 3 ale DODATKOWO z pominięciem cyfry 6
i = 10
while True:         #tak długo aż jest True
    if i == 6:      #jeśli i dojdzie do 6
        i -= 1      #to zmniejszaj i 0 1
        continue    #do tego momentu jest NIEZALEZNA PIERWSZA CZESC KODU CZYLI MAMY POMINIECIE 6
    print(i, end = '')         #1098754321  A OD TEGO MOMENTU JEST DRUGA CZESC KODU CZYLI DODATKOWO ZATRZYMANIE NA 0
    i -= 1
    if i == 0:
        break

print()

#odlicz od 1 10 trzema sposobami za pomocą pętli while,  w przypadku continute pomin cyfrę 10

x = 1
while x <=10:
    print(x, end = '')          #12345678910
    x +=1

print()

x = 1
while True:
    print(x, end = '')          #12345678910
    x += 1
    if x == 11:
        break

print()

x = 1
while True:
    if x == 10:
        continue
    print(x, end ='')
    x += 1
    if x == 11:
        break

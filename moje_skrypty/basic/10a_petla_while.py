x = 10
#przykład 1
while x > 0:        #tak długo aż x > 0 to rób
    print(x)
    x -= 1          #odejmowanie 1 od wartośći x

#przykład 2
i = 10
while True:         #tak długo aż jest True
    print(i)        #wypisuj i
    i -= 1
    if i == 0:
        break

#przykład 3
i = 10
while True:         #tak długo aż jest True
    if i == 6:
        i -= 1
        continue    #opuszcza to co jest za tym

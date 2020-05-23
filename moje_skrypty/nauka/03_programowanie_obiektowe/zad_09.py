try:
    num = float(input("Wprowadz liczbe: "))                 #gdy damy 't'
except ValueError as e:             #treść błędu zapisywana jest do zmiennej e, którą można później wyświetlić
    print("Wyjasnienie bledu", e)                           #to pojawi sie: Wyjasnienie bledu could not convert string to float: 't'
print("Dalsza czesc programu")                              #Dalsza czesc programu

#To nie jest liczba
#Wyjasnienie bledu: could not convert string to float: 'a'


def przywitanie(name="World!"):
    if name == "xxx":
        return "Nie używamy brzydkich słów!"        #dgyby w funkcji było "xxx" to pojawi się ten napis
    return f"Hello {name}"                          #a w przeciwnym wypadku domyślny napis
#to zwraca return więc funkcja musi być wyprintowana

print(przywitanie())                                #Hello World!
print(przywitanie("Rafał"))                         #Hello Rafał

#wartości domyślne
def incrementator(poczatek, krok=1):
    return poczatek + krok
print(incrementator(10))                            # 11
print(incrementator(14, 4))                         # 18

print()

def decrement(n):
    if n == 0:          #to jest osobna instrukcja, jeśli n to 0
        print("Koniec") #wyprintuj "Koniec"
    print(n)            #pierwszy obrót, n=10 i n ustawiane na 9, drugi obrót n=9 i n ustawiane na 8, ostatni obrót n=1 i n ustawiane na 0, warunek jeśli 0 to wyświetlić i zwrócić a więc 0 także będzie wyświetlone
    decrement(n-1)

decrement(10)

# 5! = 5*4! = 5*4*3! = ... = 5*4*3*2*1*0! = 120

print()

def countdown(n):
  if n == 0:
    print('Blastoff!')
    return              #opcjonalne
  else:                 #opcjonalne
    print(n)
    countdown(n - 1)

countdown(5)


zmniejsz(n)

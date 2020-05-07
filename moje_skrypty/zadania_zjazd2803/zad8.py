#Napisz program który obliczy wszystkie pierwiastki rzeczywiste równania kwadratowego o postaci ax2+bx+c=0,
# gdzie a, b i c podaje użytkownik. Program powinien na początku sprawdzić,
# czy wprowadzone równanie jest rzeczywiście kwadratowe.

#czy równanie jest kwadratowe: czy ax2+bx+c=0
a = int(input("Podaj liczbę a: "))
if a == 0:
    print("to nie jest równianie kwadratowe")
else:
    b = int(input("Podaj liczbę b: "))
    c = int(input("Podaj liczbę c: "))
    #każde równanie można rozwiązać obliczając deltę
    delta = b *b - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / ( 2 * a)
        x2 = (-b - delta ** 0.5) / ( 2 * a)
        print(f"Są dwa pierwiastki rzeczywiste: {x1} i {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Jest jeden pierwiastek rzeczywisty: {x}")
    else :
        print("Równanie nie ma pierwiastka rzeczywistego: ")

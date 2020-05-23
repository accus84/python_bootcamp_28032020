#wyjątki
#przy definiowaniu swoich wyjątków trzeba utworzyć klasę ze swoim wyjątkiem

class ExceptionFull(Exception):                                 #(Exception) trzeba dodać żeby było wiadomo że to wyjątek
    pass

class Pojemnik:
    def __init__(self, capacity):
        self.elements = []
        self.capacity = capacity

    def add_element(self, element):
        if 5 in self.elements:
            raise ValueError("Nie możemy tu mieć 5-ki")
        if len(self.elements) == 3:
            raise ExceptionFull("Capacity przekroczone")
        self.elements.append(element)           #do tablicy emenents dodaję element

p = Pojemnik(3)                                 #tworze obiekt klasy Pojemnik o capacity=3
#print(p.elements)                               #[] tablica elements jest na razie pusta
#p.add_element(2)                                #[2] dodaje 2 do tablicy
#print(p.elements)
#p.add_element(5)                                #próbuję dodać 5, pojawi się błąd:
#    raise ValueError("Nie możemy tu mieć 5-ki")
#ValueError: Nie możemy tu mieć 5-ki

#a tera drugi wyjątek:

#p.add_element(3)
#print(p.elements)                               #[2, 3]
#p.add_element(8)
#print(p.elements)                               #[2, 3, 8]
#p.add_element(4)                                #tu pojawi się błąd bo jest próba przekroczenia długości 3:
#    raise ExceptionFull("Capacity przekroczone")
#__main__.ExceptionFull: Capacity przekroczone

try:
    for i in range(6):
        p.add_element(i)
except ExceptionFull:
    print("Więcej nie można dodać")             #Więcej nie można dodać
except ValueError:
    print("Ktoś tam znowu wrzucił 5-kę")
print(p.elements)                               #[0, 1, 2]

#przykład 2

import pytest
class MyException(Exception):                   #(Exception) trzeba dodać w przypadku własnego wyjątku - wtedy wiadomo, że to wyjątek
    pass

def func_with_exception(arg):
    if arg == 1:
        raise MyException()
    else:
        raise ValueError()

#func_with_exception(1)                         #pojawia się exception: raise MyException()
#func_with_exception(2)                          #pojawia się exception: raise ValueError()

#def test_is_exception_raised():
#    with pytest.raises(MyException):
#        func_with_exception(1)
    #with pytest.raises(ValueError):
       # func_with_exception(300)
###ZADANIE Z ZAJEC
#Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarwej płaszczyźnie
#Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez inny wektor i liczbę), porównywania (po długości)
#oraz powinny posiadać czytelną reprezentację napisową
#Przykład użycia:
#vector_1 = Vector(x=1, y=2)
#vector_2 = Vector(x=1, y=2)
#vector_3 = vector_1 + vector_2

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                                      #wyświetlanie, zawsze będzie to wyświetlane kiedy będzie print na obiekcie Vector
        return f"<Vector: x={self.x}, y={self.y}>"

    def __add__(self, other):                               #dodawanie
        return Vector(self.x + other.x, self.y + other.y)   #WYMUSZENIE ABY WYNIK BYL TYPU VECTOR

    def __sub__(self, other):                               #odejmowanie
        return Vector(self.x - other.x, self.y - other.y)   #WYMUSZENIE ABY WYNIK BYL TYPU VECTOR

    def __mul__(self, other):                               #mnożenie
        if isinstance(other, Vector):                       #czytaj: jeśli other jest typu Vector
            return self.x * other.x + self.y * other.y      #to zwróć mnożenie przez wektory
        elif isinstance(other, (int, float)):               #a jeśli other (czyli drugi argument) jest typu int albo float
            return Vector(self.x * other, self.y * other)   #to zwróć typ Vector gdzie x jest mnożene przez tę liczbę i y jest mnożone przez tę liczbę
        else:
            raise NotImplementedError()


    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    @property
    def length(self):
        return pow(self.x ** 2 + self.y ** 2, 0.5)      #pierwiastek (x do kwadratu * y do kwadratu) dla [4,7]  = pierwiastek (16 + 49) = pierwiastek 65 = 8.06...
#############################
vector_1 = Vector(x=4, y=7)
vector_2 = Vector(x=1, y=3)
vector_3 = vector_1 + vector_2      #dodawanie
print(vector_3)                     #<Vector: x=5, y=10>

vector_3 = vector_1 - vector_2      #odejmowanie
print(vector_3)                     #<Vector: x=3, y=4>

vector_3 = vector_1 * vector_2      #mnożenie (x1*x2 + y1*y2)   czyli (4*1 + 7*3) = 25
print(vector_3)

vector_3 = vector_1 * 5             #mnożenie wektora przez liczbę czyli x= 4*5, y=7*5
print(vector_3)                     #<Vector: x=20, y=35>

print(vector_1.length)              #8.06225774829855   property uzyskujemy przez podanie obiektu i metody property
print(vector_2.length)              #3.1622776601683795

#z długości wynika, że v1>v2, sprawdźmy to więc:
print(vector_1 == vector_2)         #False  czy vector 1 == vector_2
print(vector_1 > vector_2)          #True   czy vector 1 > vector_2
#############################

class TestVector:

    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2

    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6

    def test_sub_2_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 - v2
        assert v3.x == -2
        assert v3.y == -2

    def test_mul_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        assert v1 * v2 == 1 * 3 + 2 * 4

    def test_mul_vector_int(self):
        v1 = Vector(3, 4)
        v2 = v1 * 3
        assert v2.x == 9
        assert v2.y == 12

    def test_vector_comparision(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)
        assert v2 > v1
        assert v1 < v2
        assert v1 == v3
        assert v1 != v2

    def test_length(self):
        v1 = Vector(2, 2)
        assert v1.length == pow(2 * 2 + 2 * 2, 0.5)

        v2 = Vector(5, 10)
        assert v2.length == pow(5 ** 2 + 10 ** 2, 0.5)

    def test_str(self):
        v1 = Vector(3, 4)
        assert str(v1) == "<Vector: x=3, y=4>"
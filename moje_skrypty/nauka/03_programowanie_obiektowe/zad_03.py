#Zaimplementuj klasę ElectricCar odwzorującą zachowanie samochodu elektrycznego
#Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu.
#Samochód powinien mieć także możliwości naładowania baterii.

# np. _traveled_distance - z podkreśleniem nie powinniśmny modyfikować, możemy modyfikować tylko przez metodę
# np. __traveled_distance - z dwoma podkreśleniami jeszcze bardziej chronią to co jest tam zapisane

# 2
class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range                                      #max range nie zmienia się ale sami sobie ustawiamy na początku
        self.__traveled_distance = 0                                    #początkowy dystansu ustawiamy na 0
# 4
    def drive(self, distance):                                          #distance określa ile chcę przejechać
        if self.max_range >= distance + self.__traveled_distance:       #jeśli zasięg, ktorym dysponujemy jest co najmniej taki jak dystans do pokonania i już przejechany dystans
            self.__traveled_distance += distance                        #to przejechany dystans zwiększa się o nasz dystans (i jest przechowywny na przyszłe operacje)
            return distance                                             #a zwracany jest dystans
        else:
            to_travel = self.max_range - self.__traveled_distance       #a jeśli zasięg jest mniejszy niz to co chcemy przejechać wówczas rzeczywiste przejechanie = zasięg - przejechany dystans
            self.__traveled_distance = self.max_range                   #następnie przejechany dystans ustawiany jest  maksymalnym zasięgiem (czyli zostaje 0 do przejechania bo zużyliśmy całość)
            return to_travel

    @property
    def possible_distance(self):                                        #dystans możliwy rzeczywiście do pokonania
        return self.max_range - self.__traveled_distance                #to zasięg - przejechany dystans

    def charge(self):                                                   #ta metoda powoduje wyzerowanie licznika (ustawia już przejechany dystans na 0
        self.__traveled_distance = 0

####################################################
ec = ElectricCar(100)
print(ec.max_range)                                                     #100    sprawdzenie atrybutu obiektu
print(ec.drive(70))                                                     #70     ustawiam, że tyle przejechałem
print(ec.possible_distance)                                             #30     tyle mogę jeszcze przejechać
print(ec.drive(50))                                                     #30     bo tyle faktycznie mogę przejechać
ec.charge()
print(ec.possible_distance)                                             #100    tyle mogę przejechać po nałądowaniu

####################################################

# 1 utworzenie klasy i pierwszy test
class TestElectricCar:

    def test_init(self):
        car = ElectricCar(100)
        assert car                      #sprawdza czy employee nie jest Nonen albo falsem (inaczej, sprawdza czy employee istnieje)
# 3
    def test_drive(self):
        car = ElectricCar(100)                              #może jechać 100
        assert car.drive(70) == 70                          #chcę jechać 70, jadę 70 (zostaje 30)
        assert car.drive(50) == 30                          #chcę jechać po, jadę tylko 30

# kolejne testy
    def test_drive_over_distance(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(10) == 0

    def test_charge(self):
        car = ElectricCar(50)
        assert car.drive(80) == 50
        assert car.drive(80) == 0
        car.charge()
        assert car.drive(80) == 50
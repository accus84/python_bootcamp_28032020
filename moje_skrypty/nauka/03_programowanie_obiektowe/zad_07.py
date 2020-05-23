#dziedziczenie

class Zwierze:
    def __init__(self, name):
        self.name = name
        self.krolestwo = "Zwierzęta"
        self.gromada = "SSaki"

    def przedstaw_sie(self):
        print(f"Cześć jestem, {self.name}")

zw = Zwierze("Bugs")
print(zw.name)                                      #Bugs
print(zw.krolestwo)                                 #Zwierzęta
zw.przedstaw_sie()                                  #Cześć jestem, Bugs

class Pies(Zwierze):                                #klasa Pies dziedziczy z klasy Zwierze
    def __init__(self, name, rasa):                 #klasa ma argumenty name i rase ale...
        super().__init__(name)                      #name jest dziedziczone z klasy Zwierze - super pobiera argument name z klasy Zwierze
        self.rasa = rasa                            #to należy do klasy Pies

pies = Pies("Pluto", "Owczarek Podhalański")
print(pies.name)                                    #Pluto
print(pies.rasa)                                    #Owczarek Podhalański
pies.przedstaw_sie()                                #Cześć jestem, Pluto

print(zw.krolestwo)                                 #Zwierzęta
print(zw.gromada)                                   #SSaki
print(pies.krolestwo)                               #Zwierzęta
print(pies.gromada)                                 #SSaki
print()
#zadanie
#Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee. Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi
#employee = PremiumEmployee('Jan', 'Nowak', 100.0)
#employee.register_time(5)
#employee.give_bonus(1000.0)
#employee.pay_salary()
#1500.0

class Employee:

    def __init__(self, first_name, last_name, rate_per_hour):
        self.registered_time = 0
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour

    def register_time(self, hours):
        self.registered_time = hours

    def pay_salary(self):
        if self.registered_time <= 8:
            to_pay = self.registered_time * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_time - 8) * self.rate_per_hour * 2
        self.registered_time = 0
        return to_pay


class PremiumEmployee(Employee):

    def __init__(self, first_name, last_name, rate_per_hour):
        super().__init__(first_name, last_name, rate_per_hour)
        self.bonus = 0

    def give_bonus(self, amount):
        self.bonus += amount                                    #bonus dodawany jest

    def pay_salary(self):
        to_pay = super().pay_salary()                           #to_pay to metoda pay_salary() pobierana z klasy Employee
        to_pay += self.bonus                                    #to_pay zwiększane jest także o bonus
        self.bonus = 0                                          #bonus jest teraz wyzerowany
        return to_pay

############################################
e = Employee("Mateusz", "Ostrowski", 20.00)
print(e.first_name)                                             #Mateusz
e.register_time(10)
print(e.pay_salary())                                           #240.0 (liczone już z nadgodzinami)
print(e.pay_salary())                                           #0 bo po wypłacie zeruje się licznik

p= PremiumEmployee("Mateusz", "Ostrowski", 20.00)               #teraz przypisujemy to samo ale do klasy PremiumEmployee
print(p.first_name)                                             #first_name jest dziedziczone z klasy Employee
print(p.rate_per_hour)                                          #20 rate_per_hour jest dziedziczone z klasy Employee
p.register_time(10)
p.give_bonus(300)
print(p.pay_salary())                                           #ta funkcja pobiera pay_salary z klasy Employee i dodatkowo uwzględnia bonus (300) zatem wynik to 540

############################################

class TestEmployee:

    def test_init(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee
        assert employee.first_name == "Jan"
        assert employee.last_name == "Nowak"
        assert employee.rate_per_hour == 100.0

    def test_register_time(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee.registered_time == 5

    def test_pay_salary(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.pay_salary() == 0
        employee.register_time(5)
        assert employee.pay_salary() == 500
        assert employee.pay_salary() == 0

    def test_pay_salary_overhours(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200
        assert employee.pay_salary() == 0


class TestPremiumEmployee:
    def test_init(self):
        pe = PremiumEmployee("Jan", "Nowak", 100.00)
        assert pe
        assert isinstance(pe, PremiumEmployee)
        assert isinstance(pe, Employee)

    def test_give_bonus_and_pay_salary(self):
        pe = PremiumEmployee("Jan", "Nowak", 100.00)
        pe.register_time(5)
        pe.give_bonus(1000)
        assert pe.pay_salary() == 100 * 5 + 1000
        assert pe.pay_salary() == 0
#zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.        #Employee, #rejestrowanie czasu pracy, #wypłacanie pensi
#Jeżeli pracownik bęzie pracował więcej niż 8 godzin  (podczas pojedynczej rejestracji czasu) to kolejne godziny policz jako nadgodziny
#z podwójną stawką godzinową

class Employee:

    def __init__(self, first_name, last_name, rate_per_hour):
        self.registered_time = 0                                                    #ustawienie jakiejś wartości początkowej
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour

    def register_time(self, hours):
        self.registered_time = hours

    def pay_salary(self):
        to_pay = self.registered_time * self.rate_per_hour                              #zarejestrowany czas * stawka
        if self.registered_time > 8:
            overtime = self.registered_time - 8                                         #nadgodziny to ogólny czas pracy - regulaminowe 8 godzin
            to_pay = (8 * self.rate_per_hour) + (overtime * 2 * self.rate_per_hour)
        self.registered_time = 0                                                        #po wypłacie zarejestrowany czas ustawiamy na 0 żeby nie wypłacać drugi raz
        return to_pay

################################################
employee = Employee('Jan', 'Nowacki', 20)
employee.register_time(8)
print(employee.pay_salary())
employee.register_time(10)
print(employee.pay_salary())
################################################

#napisać testy, testy muszą mieć różne nazwy
class TestEmployee:

    def test_init(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        assert employee                                                                 #sprawdza czy employee nie jest Nonen albo falsem (inaczej, sprawdza czy employee istnieje)
        assert employee.first_name == 'Jan'
        assert employee.last_name == 'Nowak'
        assert employee.rate_per_hour == 100

    def test_register_time(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.registered_time == 5

    def test_pay_salary(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 500
        assert employee.pay_salary() == 0

    def test_pay_salary_overhours(self):
        employee = Employee('Jan', 'Nowak', 100.0)
        employee.register_time(10)
        assert employee.pay_salary() == 1200


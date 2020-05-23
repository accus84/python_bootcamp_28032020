# Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.
# Przykład użycia:
# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available
# False
# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()
# True
# >>> cash_machine.withdraw_money(150)
# [100, 50]


class CashMachine:
    def __init__(self):
        self._money = []

    def put_money(self, bills):                 # funkcja dodająca banknoty (bills) do listy (self._money)
        self._money += bills                    #to nie stosujemy self.money.append(bills) tylko zapis jak po lewej     za każdym wywołaniem tej metody tabela money powiększa się o bills
        print (self._money)

    @property                                   # dekorator przechowujący zmienną dynamiczną
    def is_available(self):                     # jeśli długość listy jest większa od 0 to coś tam jest czyli is available == True)
        return len(self._money) > 0

    @property
    def money_left_simulation(self):
        return sum(self._money)

    def withdraw_money(self, amount):
        self.amount = amount
        to_withdraw = []
        for i in self._money:                   # dla każdego z banknotów znajdującysh się w liście _money
            if sum(to_withdraw) + i <= amount:  # pierwszy obrót to withdraw to 0
                to_withdraw.append(i)           # taki zapis z zppend może by zastosowany tylko jeśli jest w pętli      i dodajemy do listy to_withdraw, w tej metodzie będzie zwróconeto_withdraw
        if sum(to_withdraw) == amount:          #i musimy odjąć kasę z puli banktonotów (z tabeli money) a więc jeśli suma to_withdraw odpowiada dokładnie ilości jaką wprowadziliśmy to...
            for i in to_withdraw:               #każdy z banknotów do wypłaty...
                self._money.remove(i)           #jest usuwany z listy money
        return to_withdraw                      #ile zostało z zadeklarowanej kwoty

############################################
cm = CashMachine()
print(cm._money)                                #[]   wyświetlenie wartości atrybutu obiektu

print(cm.is_available)                          #False
print(cm.withdraw_money(100))                   #[] bo nic jeszcze nie wrzuciliśmy
cm.put_money([100,200,50,50,50,200,100])
print(cm._money)                                #[100, 200, 50, 50, 50, 200, 100]   wyświetlenie wartości atrybutu obiektu
print(cm.is_available)                          #True - teraz kasa jest w bankomacie
print(cm.withdraw_money(650))                   #[100, 200, 50, 50, 50, 200] (zostało 100)
print(cm._money)                                #100 o czym się przekonujemy
print(cm.money_left_simulation)                 #100
print(cm.is_available)                          #True
############################################

class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_available_for_empty_machine(self):
        cash_machine = CashMachine()
        assert cash_machine.is_available is False  # test jeśli is_available == False (czyli nie ma kasy)
        # assert not cash_machine.is_available

    def test_put_money(self):  # test czy zwraca True jeśli kasa jest dodana
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_machine_withdraw_money(self):
        cash_machine = CashMachine()
        assert cash_machine.withdraw_money(150) == []
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.withdraw_money(150) == [100, 50]

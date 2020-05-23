#Zaimplementuj w klasie CashMachine rzucanie wyjątków w następujących przypadkach:
#􏰀 brak miejsca na banknoty (ustal limit banknotów w bankomacie)
#􏰀 zła wartość wypłacanej sumy (musi być podzielna przez 10) 􏰀 brak odpowiednich banknotów w bankomacie
#Zaimplementuj prosty interfejs tekstowy do klasy bankomat obsługujący wszystkie wyjątki. Obsłuż także wyjątki wynikające z podania złych danych przez użytkownika.
#Przykład użycia:
#Podaj typ operacji: WYPŁATA
#Podaj kwotę do wypłacenia: 150
#BŁĄD: brak wystarczającej liczby banknotów dla kwoty 150!


#tutaj definiujemy exceptions oraz przy jakim warunku ma się pojawić błąd
#raise służy do wymuszania pojawienia się podanego wyjątku. Pierwszy argument to nazwa wyjątku drugi argument to wartość
import pytest


class BillException(Exception):                 #definiowanie exception - w przypadku własnego wyjątku
    pass


class NotEnoughBills(Exception):         #definiowanie exception
    pass


class CashMachine:
    def __init__(self, capacity=2):
        self._money = []
        self.capacity = capacity

    def put_money(self, bills):
        if len(self._money) + len(bills) > self.capacity:
            raise NotEnoughBills("Brak miejsca w bankomacie")
        self._money += bills

    @property
    def is_available(self):
        return len(self._money) > 0

    def withdraw_money(self, amount):
        if amount % 10 != 0:
            raise KeyError("Kwota powinna być podzielna przez 10")

        to_withdraw = []

        for bill in sorted(self._money, reverse=True):
            if sum(to_withdraw) + bill <= amount:
                to_withdraw.append(bill)
        if sum(to_withdraw) == amount:
            for bill in to_withdraw:
                self._money.remove(bill)
            return to_withdraw
        else:
            raise BillException(f"brak wystarczającej liczby banknotów dla kwoty {amount}!")                  #w domyśle else

#################################
cm = CashMachine()
cm.put_money([100])
print(cm._money)
cm.put_money([200])
print(cm._money)
#cm.put_money([50])          #tu tywali błąd, że nia ma miejsca w bankomacie:

#    raise NotEnoughSpacForBills("Brak miejsca w bankomacie")
#__main__.NotEnoughSpacForBills: Brak miejsca w bankomacie
#################################

class TestCashMachine:
    def test_init(self):
        cash_machine = CashMachine()
        assert cash_machine

    def test_is_available_for_empty_machine(self):
        cash_machine = CashMachine()
        assert cash_machine.is_available is False
        # assert not cash_machine.is_available

    def test_put_money(self):
        cash_machine = CashMachine()
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.is_available is True

    def test_withdraw_money(self):
        cash_machine = CashMachine()
        assert cash_machine.withdraw_money(150) == []
        # assert CashMachine.withdraw_money(cash_machine, 150) == []
        cash_machine.put_money([200, 100, 100, 50])
        assert cash_machine.withdraw_money(300) == [200, 100]

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])
        assert cash_machine.withdraw_money(300) == [200, 100]
        assert cash_machine.withdraw_money(300) == []

        cash_machine = CashMachine()
        cash_machine.put_money([50, 100, 100, 200])
        assert cash_machine.withdraw_money(600) == []

    def test_value_error_when_amount_is_not_divided_by_10(self):
        cash_machine = CashMachine()
        cash_machine.put_money([100, 100, 100])
        with pytest.raises(KeyError):
            cash_machine.withdraw_money(123)

    def test_bills_exception_when_not_enough_bill_to_withdraw(self):
        cash_machine = CashMachine()
        cash_machine.put_money([100, 100, 100])
        with pytest.raises(BillException):
            cash_machine.withdraw_money(150)

    def test_not_enought_room_for_bills(self):
        cm = CashMachine(capacity=10)
        with pytest.raises(NotEnoughSpacForBills):
            cm.put_money([100 for i in range(20)])
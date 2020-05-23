#tutaj obsługujemy wyjątki

from bankomat import CashMachine, NotEnoughSpacForBills, BillException

cash_machine = CashMachine(capacity=3)
cash_machine.put_money([200, 200, 100, 100])        #tu wywali ten sam błąd:

#    raise NotEnoughSpacForBills("Brak miejsca w bankomacie")
#bankomat.NotEnoughSpacForBills: Brak miejsca w bankomacie

while True:
    operation = input("Podaj typ operacji: [wplata, wyplata, koniec]: ")
    if operation == "koniec":
        break
    elif operation == "wplata":
        bills = input("Podaj liste banknotów rozdzielajac je przecinkiem np:100,100,50,50:  ")      #w bankomacie jest już 6 banknotów, limit to 8 banknotów zatem przy próbie dodania od 3 banknotów wywali błąd
        bills = bills.split(",")
        bills = [int(bill) for bill in bills]
        try:
            cash_machine.put_money(bills)
        except NotEnoughSpacForBills as e:  #jak wywali taki błąd to jest przekazanie tego exception do zmiennej e
            print("Error: ", e)             #wypisanie exception pod zmienną e
    elif operation == "wyplata":
        amount =int(input("Podaj kwotę do wypłaty: "))
        try:                                                    #próbujemy coś zrobić
            bills = cash_machine.withdraw_money(amount)
        except BillException as e:
            print("Błąd: ", e)
        except KeyError as e:
            print("Kwota powinna być wielokrotnością 10 PLN")



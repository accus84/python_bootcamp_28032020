#Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
#Przykład użycia:
#>>> product = Product(1, 'Woda', 10.99)
#>>> product.print_info()
#Produkt "Woda", id: 1, cena: 10.99 PLN

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        text = f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN"
        print(text)
        return text

###########################################
produkt = Product(5, 'ziemniaki', 7.99)         #tworzymy obiekt klasy Product, podajemy argumenty obiektu
produkt.print_info()                            #teraz możemy wyświetlić metodę obiektu
produkt2 = Product(5, 'gruszki', 4.49)
produkt2.print_info()
###########################################

class TestProduct:
    def test_init(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt
        assert produkt.id == 1
        assert produkt.name == "Woda"
        assert produkt.price == 10.99

    def test_print_info(self):
        produkt = Product(1, "Woda", 10.99)
        assert produkt.print_info() == "Produkt \"Woda\", id: 1, cena: 10.99 PLN"

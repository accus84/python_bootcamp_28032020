#Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
#Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
#Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.
#Przykład użycia:
#>>> basket = Basket()
# >>> product = Product(1, 'Woda', 10.00) >>> basket.add_product(product, 5)
# >>> basket.count_total_price()
# 50.0
# >>> basket.generate_report()
#'Produkty w koszyku:\n
#- Woda (1), cena: 10.00 x 5\n
#W sumie: 50.00'

## w tym zadaniu chodzi o to ze kazdy produkt wkladamy do osobnego pudelka (niezaleznie jaka jest jego ilosc)

## !!! self.product.price - jak jestem w innej klasie np to jak sie odwoluje do obiektu inej klasy ro robie self.(innaklasa).(obiekt tej innej klasy)
## w tym zadaniu chodzi o to ze kazdy produkt wkladamy do osobnego pudelka (niezaleznie jaka jest jego ilosc)

class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product, amount):
        self.products.append(BasketEntry(product, amount))                  #dodawanie do listy products (powyżej pusta lista) z klasy BasketEntry (BasketEntry poprostu wypisuje co jest w baskecie)

    def count_total_price(self):
        total_price = 0
        for i in self.products:                                             #dla każdego z produktów
            total_price += i.price                                          #do total price dodajemy cenę każdego z produktów
        return total_price
        # return sum([be.price for be in self.products])

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for i in self.products:
            report += i.report
        report += f"W sumie: {self.count_total_price():.2f}"
        return report

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class BasketEntry:                                                      #w tej klasie argument product jest typu argumentów klasy Product
    # pokazano tu przykład adnotacji - określenie typów argumentów
    def __init__(self, product: Product, amount: int):                  #":Product" i ": int" to taka podpowiedz która mówi jakiego typu są argumenty - ciekawostka. To przykład adnotacji - określenie typów argumentów
        self.product = product                                          #inaczej mówiąć product korzysta z klasy Product czyli można zrobić product.name, product.id, product.price
        self.amount = amount

    @property
    def price(self):
        return self.amount * self.product.price

    @property
    def report(self):
        return f"- {self.product.name} ({self.product.id}), cena: {self.product.price:.2f} x {self.amount}\n"

##############################################################################################
#klasa Product przedstawia (szczegółowo) id, nazwę i cenę produktu
p = Product(1, 'Woda', 10.00)
print(p.id)                                                             #1
print(p.name)                                                           #Woda
print(p.price)                                                          #10.00
print()
#klasa BasketEntry przedstawia nazwę produktu, ilość i cenę za łączną ilość (liczba * cena z klasy Product)
be = BasketEntry(p, 25)                                                 #p jest obiektem klasy Product zatem pierwszym argumentem klasy BasketEntry jest p
print(be.product)                                                       #<__main__.Product object at 0x031AC310>
print(be.amount)                                                        #25
print(be.price)                                                         #250
print(be.report)                                                        #- Woda (1), cena: 10.00 x 25
print()
#klasaBasket
b = Basket()
p2 = Product(2, 'ziemniaki', 4.99)                                      #[]     produkty aktualnie w basket
b.add_product(p, 50)
b.add_product(p2, 100)
print(b.count_total_price())                                            #250.0      999.0
print(b.generate_report())
##############################################################################################

class TestBasket:
    def test_init(self):
        basket = Basket()
        assert basket
        assert basket.products == []

    def test_add_product(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)
        assert len(basket.products) == 1
        assert basket.products[0].product == product
        assert basket.products[0].amount == 5

    def test_count_total_price(self):
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        product2 = Product(2, "Chleb", 2)
        basket.add_product(product, 5)
        basket.add_product(product2, 5)
        assert basket.count_total_price() == 5 * 10.0 + 5 * 2

    def test_generate_report(self):
        expected = '''Produkty w koszyku:
- Woda (1), cena: 10.00 x 5
W sumie: 50.00'''
        basket = Basket()
        product = Product(1, "Woda", 10.00)
        basket.add_product(product, 5)                      #jakiś produkt w jednym pudełku  w ilości 5 sztuk (np 5 wód w pudełku)
        assert basket.generate_report() == expected


class TestProduct:
    def test_init(self):
        product = Product(1, "Woda", 10.00)
        assert product.id == 1
        assert product.name == "Woda"
        assert product.price == 10.00


class TestBasketEntry:
    def test_init(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)                        #wkładam 5 takich maseł do pudełka
        assert be.product == product
        assert be.amount == 5

    def test_price(self):                               #jaki jest koszt pudełka z produktem
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.price == 5 * 8

    def test_report(self):
        product = Product(2, "masło", 8)
        be = BasketEntry(product, 5)
        assert be.report == '- masło (2), cena: 8.00 x 5\n'




import time
#dokorator korzysta z metody klasy (musi być taka sama nazwa dekoratora i metody), która z kolei ma argument jako funkcję. Tą funkcją metody jest dekorator.
#dekorator może być także użyty jako odrębna metoda która będzie coś zwracała

def milion_kwadratow():
    return len([x**2 for x in range(1000000)])


def mierz_czas(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start)
        return result

    return wrapper

@mierz_czas
def kwadraty(n):
    return len([x ** 2 for x in range(n)])

milion_kwadratow = mierz_czas(milion_kwadratow)

kwadraty(1000000)
milion_kwadratow()


# start = time.time()
# print(milion_kwadratow())
# print(time.time() - start)
#
# start = time.time()
# print(kwadraty(10000000))
# print(time.time() - start)
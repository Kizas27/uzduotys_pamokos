#printinam stringa y console
print("labas rytas")

#is github
print("is github")

# taip sukuriamas exception
'''
#raise Exception("kazkas yvyko (error)")

# cia sitas prie error is temos exception p.s. visi printai uzkomentuoti
import random
klaidu_sarasas = [IndexError, SyntaxError, KeyboardInterrupt]

def random_exception(sarasas):
    raise random.choice(sarasas)

erorr_count = {}
#\cia (x=) tas pats kaip (for klaidu_tipas......)
#x = {klaidu_tipas: 0 for klaidu_tipas in klaidu_sarasas}
#print(x)

for klaidu_tipas in klaidu_sarasas: #cia padaromas dict su klaidu tipais
    erorr_count[klaidu_tipas] = 0
#print(erorr_count)

for i in range(10):
    try:
        random_exception(klaidu_sarasas)

    except IndexError:
        #print(f"pagautas index error")
        erorr_count[IndexError] += 1

    except SyntaxError:
        #print(f"pagautas Syntax error")
        erorr_count[SyntaxError] += 1

    except KeyboardInterrupt:
        #print(f"pagautas Keyboard error")
        erorr_count[KeyboardInterrupt] += 1

#print(f"Gautas rezulatatas: {erorr_count}")
'''

# pasiekti listo pirma elementa my_list[0]
'''my_list =["labas"]
print(my_list[0])
'''

#funkcijos kurimas
'''
def name():
    print()
'''
#loggerio i console kurimas
'''
#logging levelname(CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0)
import logging

l = logging.getLogger("LOGGERIS i console")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(levelname)s %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)
#loggerio kurimas i faila

import logging
l = logging.getLogger("LOGGERIS i faila.log")
h = logging.FileHandler("failas.log")
f = logging.Formatter("%(asctime)s: [%(levelname)s] %(message)s faile: %(filename)s eiluteje: %(lineno)s")
h.setFormatter(f)
l.setLevel(logging.INFO)
l.addHandler(h)
#cia perduoda i failas.log
l.critical("auksciausias loggas 50")
l.error("error logas 40")
l.warning("warning logas 30")
l.info("info logas 20")
l.debug("debug logas 10")
'''

#class kurimas

class Car:
    model = ""
    price = 0.0
    year = 0

    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year
    def __str__(self):
        return (f"{self.brand}: {self.model} year: {self.year} price: {self.price}")

#subclass kurimas
class Audi(Car):
    brand = "Audi"
    def __init__(self, model, price, year):
        super().__init__(model, price, year)

#car =Audi("a6", 1000.00, 1999)
#print(car)

#dekoratoriaus kurimas per class
class HTMLHeader:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return f"<h1>{result}</h1>"


@HTMLHeader
def prepare_title(title_string):
    return title_string.title() # .title() padaro kiekviena zody is didziosios raides


if __name__ == "__main__":
    print(prepare_title("this is a section title!"))

# dekoratorius per classe su functtools

import functools


class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self.multiplier  #is funcijos(double_addition) paimtas atsakymas ir atliekama dekoratoriuje daugyba

        return wrapper


@Multiply(2)
def double_addition(a, b):
    return a + b


@Multiply(3)
def triple_addition(a, b):
    return a + b


if __name__ == "__main__":
    print(double_addition(2, 2))
    print(triple_addition(1, 1))

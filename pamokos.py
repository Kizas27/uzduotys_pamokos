#printinam stringa y console
def i_console():
    print("labas rytas")

#is github
def is_github():
    print("is github")


# pasiekti listo pirma elementa my_list[0]
def listai():
    my_list = ["labas"]
    print(my_list)
    my_list.append("Vakaras")
    print(my_list)
    print(my_list[0], my_list[1])

#loggerio i console kurimas
def logingas():
                #logging levelname(CRITICAL=50, ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0)
    import logging
    #loggingas y console
    l = logging.getLogger("LOGGERIS i console")
    h = logging.StreamHandler()
    f = logging.Formatter("%(asctime)s: %(levelname)s %(message)s")
    h.setFormatter(f)
    l.addHandler(h)
    l.setLevel(logging.INFO)
    l.critical("auksciausias loggas 50")
    l.error("error logas 40")
    l.warning("warning logas 30")
    l.info("info logas 20")
    l.debug("debug logas 10")

    #loggerio kurimas i faila
    import logging
    l = logging.getLogger("LOGGERIS i faila.log")
    h = logging.FileHandler("logging.log")
    f = logging.Formatter("%(asctime)s: [%(levelname)s] %(message)s faile: %(filename)s eiluteje: %(lineno)s")
    h.setFormatter(f)
    l.setLevel(logging.INFO)
    l.addHandler(h)
    #cia perduoda i failas.log
    #l.critical("auksciausias loggas 50")
    #l.error("error logas 40")
    #l.warning("warning logas 30")
    #l.info("info logas 20")
    #l.debug("debug logas 10")

def generator_1():
    cars = ["Audi", "VW", "BMW", "Mercedes-Benz"]
    cars_iterator = iter(cars)
    print("Cars Iterator")
    print(cars_iterator.__next__())  # or
    print(next(cars_iterator))

def generator_2():
    cars = ["Audi", "VW", "BMW", "Mercedes-Benz"]
    cars_iterator = iter(cars)
    for c in cars_iterator:
        # next(cars_iterator)       # isprintins viska kas yra iteratoriuje
        # (taciau jei pries jy yra iteratorius ir paimtas su next tai tes nuo ten kur baige iteratriu)
        print(c)

def generator_3():
    class MyRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step

        def __iter__(self): ## cia iskvieciamas iteratorius
            self.start -= self.step
            return self

        def __next__(self):
            self.start += self.step
            if self.start < self.stop:
                return self.start
            else:
                raise StopIteration

    for i in MyRange(0, 10, 1):
        print(i)

def generators_4(num):
    def fib():
        a = 0
        b = 1
        while True:
            yield a
            a, b = b, a + b

    def parameter(gen, max_num):
        # i = 0
        for i in range(1, max_num):
            yield next(gen)

    for i, elem in enumerate(parameter(fib(), num)):
        print(f"fib({i}): {elem}")


# taip sukuriamas exception
def exceptionas():
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
    print(erorr_count)

    for i in range(10):
        try:
            random_exception(klaidu_sarasas)

        except IndexError:
            print(f"pagautas index error")
            erorr_count[IndexError] += 1

        except SyntaxError:
            print(f"pagautas Syntax error")
            erorr_count[SyntaxError] += 1

        except KeyboardInterrupt:
            print(f"pagautas Keyboard error")
            erorr_count[KeyboardInterrupt] += 1

    print(f"Gautas rezulatatas: {erorr_count}")

def exceptionas2():
    import random

    posible_exception = [OSError, IndexError, NameError, ValueError, KeyboardInterrupt]

    def example_exception():
        raise Exception("Message about exception: 'This is a manually raised exception!'")

    def try_exception():
        try:
            print("Labas")
            print("Vakaras")
            raise Exception("O ne! Dabar diena")
            print("Naktis")
        except Exception:
            print("As labai atsiprasau")

    def random_exception(list_of_error):
        raise random.choice(list_of_error)

    """
    Given function random_exception which raises a random exception every time,
    write a try-except block which handles each of the possible exceptions by
    counting their occurrences. Print the tally.
    """

    def random_exception_count(ranges):
        error_count = dict()
        for error_type in posible_exception:
            error_count[error_type] = 0

        for i in range(ranges):
            try:
                random_exception(posible_exception)
            except OSError:
                error_count[OSError] += 1
            except IndexError:
                error_count[IndexError] += 1
            except NameError:
                error_count[NameError] += 1
            except ValueError:
                error_count[ValueError] += 1
            except KeyboardInterrupt:
                error_count[KeyboardInterrupt] += 1
        return error_count



    """
    1. Define your own exceptions:
        1. `PasswordTooShort`
        2. `PasswordTooLong`
        3. `InvalidPassword`
    2. Write a function `validate_password()`:
        1.  check whether user input collected via `input()` equals 
            `secret_password` variable.
        2. If the input is too short (less than 3 characters) or too long
           (longer than 30 characters), raise appropriate exceptions
        3. If the password does not match, raise `InvalidPassword`
    3. Handle all exceptions raised in `validate_password` by printing a 
       nice message.
    """

    class PasswordTooShort(Exception):
        pass

    class PasswordTooLong(Exception):
        pass

    class InvalidPassword(Exception):
        pass

    def validate_password():
        correct_pass = "slapikas"
        input_pass = input("Please input your passwrod: ")
        if len(input_pass) < 3:
            raise PasswordTooShort
        if len(input_pass) >= 30:
            raise PasswordTooLong
        if input_pass != correct_pass:
            raise InvalidPassword
        print("Jusu slaptazodis teisingas")

    def password_checker():
        try:
            validate_password()

        except PasswordTooShort:
            print("Your password to short!!!")

        except PasswordTooLong:
            print("Your password to long!!!")

        except InvalidPassword:
            print("Password Invalid!!!")

    try_exception()
    print(random_exception_count(ranges=25))
    password_checker()

#class kurimas
def klases():
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

    car =Audi("a6", 1000.00, 1999)
    print(car)

#dekoratoriaus kurimas per class
def dekoratorius_per_klase():
    class HTMLHeader:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            result = self.func(*args, **kwargs)
            return f"<h1>{result}</h1>"

    @HTMLHeader
    def prepare_title(title_string):
        return title_string.title() # .title() padaro kiekviena zody is didziosios raides

    print(prepare_title("this is a section title!"))


# dekoratorius per classe su functtools
def dekoratorius_su_functools():
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

    print(double_addition(2, 2))
    print(triple_addition(1, 1))


if __name__ == "__main__":
    print("printas y console:")
    i_console()
    print()
    print("ykelta is github:")
    is_github()
    print()
    print("Exceptionai (isimtis, priestaravimai):")
    exceptionas()
    exceptionas2()
    print()
    print("Listai:")
    listai()
    print()
    print("Loggingai:")
    logingas()
    print()
    print("Generatoriai:")
    generator_1()
    generator_2()
    generator_3()
    generators_4(num=10)
    print()
    print("Klases:")
    klases()
    print()
    print("Dekoratorius:")
    dekoratorius_per_klase()
    print()
    print("Dekoratorius su functools:")
    dekoratorius_su_functools()
    print()


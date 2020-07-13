import random
class Zaidejas():
    name = ""
    position = 0

    def __init__(self, name, position=0):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} {self.position}"
    def __repr__(self):
        return f"{self.name}"
def random_skaicus():
    return random.randrange(1,7)
    pass

if __name__ == "__main__":
    zaideju_sarasas = []
    random_skaicius = 0
    print(random_skaicius)
    while random_skaicius != 6:
        print(random_skaicius)
        random_skaicius = random_skaicus()

    zaideju_kiekis = int(input("Kaik ziaideju: "))
    zaidejas = Zaidejas("vaidas", 15)
    print(zaidejas)
    for i in range(zaideju_kiekis):
        name = input("Iveskite zaidejo varda: ")
        zaideju_sarasas.append(Zaidejas(name))

    print(zaideju_sarasas)
    #while True:

    if Zaidejas.position >= 2:
        print(Zaidejas.name, " Jus laimejote")

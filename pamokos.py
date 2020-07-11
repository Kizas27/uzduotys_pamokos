#printinam stringa y console
print("labas rytas")

def suma(x, y):
    return x + y


print(suma(5, 6))

#is github
print("is github")


# taip sukuriamas exception
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



# pasiekti listo pirma elementa my_list[0]
my_list =["labas"]
print(my_list[0])

#funkcijos kurimas
def name():
    print()


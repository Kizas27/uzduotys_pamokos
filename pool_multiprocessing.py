import multiprocessing
import random

def calculator(a, b, c):
    return a + b + c

def saukiam():
    arguments_list = [
        (random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))
        for i in range(500) #for ciklas sukuria liste 500 tuple sdarasa
        ]
    multiprocessing.Pool()
    with multiprocessing.Pool(10) as worker:
        result = worker.starmap(calculator, arguments_list)
    for i in range(5):
        print(f"{arguments_list[i]} --> {result[i]}")
    print("............")
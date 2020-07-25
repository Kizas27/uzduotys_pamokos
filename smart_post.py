class Spintele:
    __password = ""
    location = []

    def __init__(self, password):
        self.__password = password

    def __str__(self):
        return f"{self.__password}"

    def get_password(self):
        return f"{self.__password}"

class Parcel(Spintele):
    def __init__(self, password):
        super().__init__(password)

def input_password():
    inpu = "Iveskite slaptazody"
    pasword = input(inpu)
    return pasword

def check_password(paswd):
    if paswd == in_password._Spintele__password:
        print("Slaptazodis teisingas")
    else:
        print("Ivestas slapazodis neteisingas")
        pass
in_password = Parcel(input_password())
check_password("123456")
class user:
    def __init__(self, nume, nivel_acces="Default"):
        self._nume = nume
        self.__nivel_acces = nivel_acces

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, valoare):
        self._nume = valoare

    @property
    def nivel_acces(self):
        return self.__nivel_acces

    @nivel_acces.setter
    def nivel_acces(self, valoare):
        self.__nivel_acces = valoare


class Sistem:
    def __init__(self):
        self.__utilizatori = {}

    def adauga_utilizator(self, utilizator):
        id_utilizator = len(self.__utilizatori) + 1
        self.__utilizatori[id_utilizator] = utilizator

    def afiseaza_utilizatori(self):
        return [utilizator.nume for utilizator in self.__utilizatori.values()]

    def verifica_nivel_acces(self, nume_utilizator):
        for utilizator in self.__utilizatori.values():
            if utilizator.nume == nume_utilizator:
                return utilizator.nivel_acces
        return "Utilizatorul nu există."

    def modifica_name_user(self, id_utilizator, nume_nou):
        if id_utilizator in self.__utilizatori:
            self.__utilizatori[id_utilizator].nume = nume_nou
        else:
            return "Utilizatorul nu există."

    def sterge_utilizator(self, id_utilizator):
        if id_utilizator in self.__utilizatori:
            del self.__utilizatori[id_utilizator]
        else:
            return "Utilizatorul nu există."

    def modifica_nivel_acces(self, id_utilizator, nivel_nou):
        if id_utilizator in self.__utilizatori:
            self.__utilizatori[id_utilizator].nivel_acces = nivel_nou
        else:
            return "Utilizatorul nu există."


u1 = user('gigi')
u2 = user('hhfhfh')
u3 = Sistem()
u3.adauga_utilizator(u1)
u3.adauga_utilizator(u2)
print(u3.afiseaza_utilizatori())
print(u3.verifica_nivel_acces('gigi'))
u3.modifica_name_user(1, 'becali')
print(u3.afiseaza_utilizatori())
u3.sterge_utilizator(2)
print(u3.afiseaza_utilizatori())
u3.modifica_nivel_acces(1, "mare")
print(u3.verifica_nivel_acces(''))

class Animal:

    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        pass


class Perro(Animal):

    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        print("Wawww")


class Gato(Animal):

    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        print("Miau")


class Raton(Animal):

    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        print("Zxzxzx")


class Tigre(Animal):

    def __init__(self) -> None:
        super().__init__()

    def hablar(self):
        print("GRRARRRR")


dog = Perro()
cat = Gato()
mice = Raton()
tiger = Tigre()

animals = [dog, cat, mice, tiger]

""" Cada animal en particular hereda de la clase Animal. La cual tiene definio el metodo hablar()"""
""" Pero cada animal tiene su propia implementacion del metodo hablar(), pero entre ellos comparten la misma firma / interface"""
for animal in animals:
    animal.hablar()

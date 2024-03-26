#!/usr/bin/python3

from mammal import Mammal #se importa desde el archivo mammal.py

class Dog(Mammal):
    def __init__(self, color='gray') -> None:
        super().__init__(color)
    def make_sound(self) -> None:
        if self._mood<0:
            print('grr')
        else:
            print('wuff')


if __name__=="__main__":
    scooby=Dog()
    scooby.beat()

    mammal = Mammal()
    mammal.beat()
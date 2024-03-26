#!/usr/bin/python3

class Mammal:
    def __init__(self, color='gray') -> None:
        self.color=color
        self._mood = 5
    def _change_mood(self,change)->None:
        self._mood += change
        self.make_sound()
    def make_sound(self)->None:
        raise NotImplemented  #los mamíferos pueden hacer diferentes sonidos
        #make_sound todaví no está implementada porque se hará en las clases hijas
    def pat(self)->None:
        self._change_mood(1)
    def beat(self)->None:
        self._change_mood(-1)
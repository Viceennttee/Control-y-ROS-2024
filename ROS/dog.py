#!/usr/bin/python3
#shebag line
#línea que tienen todos los scripts para ver cual es su interprete

class dog:
    def __init__(self, color: str='brown') -> None:
        self.color=color#atributo publicpo
        self._mood=5 #humor del perro que es privado por el "_"
        pass
    def make_sound(self)->None:
        if self._mood<0:
            print("wuff")
        else:
            print('feliz')
    def change_mood(self,change)->None:
        self._mood+=change
        self.make_sound()
    def pat(self)->None:
        self.change_mood(1)
    def beat(self)->None:
        self.change_mood(-3)








"""
Entry point, define el punto de inicio de una función 
"""
if __name__=="__main__":
    print("code executed ..")

    #declaracion de objetos
    snoopy=dog('blanco')
    scooby=dog()


    #miembro función
    snoopy.make_sound()
    print(snoopy.color)
    snoopy.color='amarillo'
    print(snoopy.color)
    print(snoopy._mood)
    snoopy.beat()
    print(snoopy._mood)
    snoopy.beat()
    snoopy.beat()
    snoopy.beat()
    print(snoopy._mood)



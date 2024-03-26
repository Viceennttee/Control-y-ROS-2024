#!/usr/bin/python3


class Dog:
    #atributos de la clase(variables globales)
    legs =4
    all_dogs=set() #también es una lista o arreglo, solo que no permite elementos repetidos
    


    def __init__(self, name, color="brown") -> None:
        self._color=color
        self._name =name
        self._mood=5

        Dog.all_dogs.add(self) #agregar cada instancia creada al set

#un metodo mágico empieza con __
# se sobreescribe la función imprimir para esa clase en particulas
    def __repr__(self)->str:
        return self._name
    

# se redefine len
    def __len__(self)->int:
        return 5
    
    def _get_mood(self)-> str:
        if self._mood<0:
            return 'angry'
        return 'happy'
    #siempre que se puede evitar el uso de los else hay que hacerlo 



    #se revisa si el valor esta en el rango y si no lo está se levanta un error 
    def _set_mood(self, value) ->None:
        if not -10 <= value <=10:
            raise ValueError('Bad range')
        self._mood = value
    

    mood  = property(_get_mood,_set_mood)

if __name__ == '__main__':
    print(len(Dog.all_dogs))
    snopy = Dog('loki','white')



    snopy.legs=2
    print(Dog.legs,snopy.legs)
    print(snopy)
    print(len(snopy))

    print('snopy mood is ',snopy.mood)
    snopy.mood=-5
    print('snopy mood is ',snopy.mood)

    print(Dog.all_dogs)

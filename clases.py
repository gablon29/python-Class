class Persona(): 
    # inicializamos el constructor
    # con los atributos de instacia "name, friend" que seran tomados como parametros por el constructor.
    def __init__(self, name, friend):
        self.name = name
        self.friend = friend
        # Creamos un metodo para setear el estado de friend.
    def fight(self, stateFriend):
        self.friend = stateFriend
        # creamos un metodo para imprimir por consola los valores de los atributos de instacia.
    def mostrarObj(self):
        return f"Persona: {self.name}, Amigo: {self.friend}"
    
gabriel = Persona('Gabriel', True)
gabriel.fight(False)
gabriel.mostrarObj()

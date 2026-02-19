class Nodo:
    def __init__(self,documento, nombre):
        self.documento=documento
        self.nombre=nombre
        self.siguiente=None

class lista:
    def __init__(self):
        self.cabeza=None
    def AgregarAlFinal(self, documento, nombre):
        nodo=Nodo (documento, nombre)
        if self.cabeza==None:
            self.cabeza=nodo
        else:
            actual=self.cabeza
            while actual.siguiente != None:
                actual=actual.siguiente
            actual.siguiente=nodo    
        #mejora
'''class Nodo:
    def __init__(self,documento, nombre):
        self.documento=documento
        self.nombre=nombre
        self.siguiente=None
        self.cola=None        

class lista:
    def __init__(self):
        self.cabeza=None
    def AgregarAlFinal(self, documento, nombre):
        nodo=Nodo (documento, nombre)
        if self.cabeza==None:
            self.cabeza=nodo
            self.cola=nodo
        else:
            self.cola.siguiente=nodo
            self.cola=nodo    
'''
class Node:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:

    # Constructor que define el estado inicial de la lista
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    # Verifica si la lista esta vacia
    def vacia(self):
        return self.primero == None

    # Agrega un nuevo nodo al final de la lista
    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Node(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Node(dato)
            self.ultimo.anterior = aux
        self.size += 1

    # Agrega un nuevo nodo al inicio de la lista
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Node(dato)
        else:
            aux = Node(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.size += 1

    # Recorre la lista desde izquierda a derecha
    def recorrer_inicio(self):
        if self.vacia():
            print("La lista esta vacia")
        else:
            aux = self.primero
            while aux != None:
                print(aux.dato)
                aux = aux.siguiente

    # Recorre la lista desde derecha a izquierda
    def recorrer_final(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

    # Elimina el primer elemento de la lista
    def eliminar_inicio(self):
        if self.vacia():
            print("La lista esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1

    # Elimina el último elemento de la lista
    def eliminar_final(self):
        if self.vacia():
            print("La lista esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoblementeEnlazada()

        while opcion != 7:
            print(">>>MENU<<<")
            print("1. Agregar al inicio")
            print("2. Agregar al final")
            print("3. Recorrer desde el inicio")
            print("4. Recorrer desde el final")
            print("5. Eliminar del inicio")
            print("6. Eliminar del final")
            print("7. Salir")

            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                dato = input("Ingrese un numero: ")
                lista.agregar_inicio(dato)

            elif opcion == 2:
                dato = input("Ingrese un numero: ")
                lista.agregar_final(dato)

            elif opcion == 3:
                lista.recorrer_inicio()

            elif opcion == 4:
                lista.recorrer_final()

            elif opcion == 5:
                lista.eliminar_inicio()

            elif opcion == 6:
                lista.eliminar_final()

except Exception as e:
    print("Error:", e)
# Hacer un menu en terminal que muestre una listas de canciones 
# al agregar a la lista saber la duracion
# poder pasar de canciones
# saber que cancion estoy escuchando
# eliminar canciones
# buscar canciones
# me muestre la lista de las canciones
# cual esta sonando en ese momento

class Node:

    def __init__(self, nom, seg):
        self.nom = nom
        self.seg = seg
        self.siguiente = None
        self.anterior = None

class Reproductor:

    # Constructor que define el estado inicial del reproductor
    def __init__(self):
        self.primera_cancion = None # Primero
        self.ultima_cancion = None # Ultimo
        self.cancion_actual = None # Canción que esta sonando
        self.size = 0

    # Verifica si la lista esta vacia
    def vacia(self):
        return self.primera_cancion is None

    # Agrega una nueva canción a la lista
    def agregar_cancion(self, nom, seg):
        nuevo_nodo = Node(nom, seg)
        if self.vacia():
            self.primera_cancion = self.ultima_cancion = nuevo_nodo
        else:
            self.ultima_cancion.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultima_cancion
            self.ultima_cancion = nuevo_nodo
        self.size += 1
        print("Canción agregada: ", nuevo_nodo.nom)

    # # Elimina una canción de la lista desde el lado izquierdo
    # def eliminar_cancion_izquierda(self, nom):
    #     if self.vacia():
    #         print("La lista esta vacia")
    #     elif self.primera_cancion.siguiente == None:
    #         self.primera_cancion = self.cancion_actual = None
    #         self.size = 0
    #     else:
    #         self.primera_cancion = self.primera_cancion.siguiente
    #         self.primera_cancion.anterior = None
    #         self.size -= 1

    # # Elimina una canción de la lista desde el lado derecho
    # def eliminar_cancion_derecha(self, nom):
    #     if self.vacia():
    #         print("La lista esta vacia")
    #     elif self.primera_cancion.siguiente == None:
    #         self.primera_cancion = self.cancion_actual = None
    #         self.size = 0
    #     else:
    #         self.primera_cancion = self.primera_cancion.siguiente
    #         self.primera_cancion.siguiente = None
    #         self.size -= 1

    # Reproduce la siguiente canción en la lista
    def siguiente_cancion(self):
        if self.vacia():
            print("La lista esta vacia")
        elif self.cancion_actual is None:
            self.cancion_actual = self.primera_cancion
            print("Reproduciendo: ", self.cancion_actual.nom)
        elif self.cancion_actual.siguiente is None:
            print("No hay más canciones adelante.")
        else:
            self.cancion_actual = self.cancion_actual.siguiente
            print("Reproduciendo: ", self.cancion_actual.nom, "Duración: ", self.cancion_actual.seg, "segundos")

    # Muestra la canción actual que se está reproduciendo
    def mostrar_actual(self):
        if self.cancion_actual is None:
            print("No hay ninguna canción reproduciéndose.")
        else:
            print("Canción actual: ", self.cancion_actual.nom, "Duración: ", self.cancion_actual.seg, "segundos")

    # Muestra la canción anterior que se estaba reproduciendo
    def cancion_anterior(self):
        if self.vacia():
            print("La lista esta vacia")
        elif self.cancion_actual.anterior is None or self.cancion_actual is None:
            print("No hay más canciones atrás. Estás en la primera.")
        else:
            self.cancion_actual = self.cancion_actual.anterior
            print("Reproduciendo: ", self.cancion_actual.nom)

    # Eliminar una canción especifica
    def eliminar_cancion(self, nom):
        if self.vacia():
            print("La lista esta vacia")
            return

        actual = self.primera_cancion
        while actual is not None:
            if actual.nom == nom:
                if actual == self.cancion_actual:
                    self.cancion_actual = None
                    print("La canción actual ha sido eliminada:", nom)

                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primera_cancion = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultima_cancion = actual.anterior
                    
                self.size -= 1
                print("Canción eliminada:", nom)
                return
            actual = actual.siguiente
        print("Canción no encontrada:", nom)

    # Buscar una canción en específico
    def buscar_cancion(self, nom):
        if self.vacia():
            print("La lista esta vacia")
            return
        
            actual = self.primera_cancion
            while actual is not None:
                if actual.nom == nom:
                    print("Canción encontrada:", nom, "Duración:", actual.seg, "segundos")
                    return
                actual = actual.siguiente
            print("Canción no encontrada:", nom)

    # Muestra la lista de canciones
    def mostrar_lista(self):
        if self.vacia():
            print("La lista esta vacia")
            return
        
        print("\nLista de canciones:")
        actual = self.primera_cancion
        posicion = 1
        while actual is not None:
            print("Canción:", actual.nom, "Duración:", actual.seg, "segundos")
            actual = actual.siguiente
            posicion += 1

if __name__ == "__main__":
    canciones = Reproductor()
    salir = False

    while not salir:
        print("\n=== REPRODUCTOR DE MÚSICA ===")
        print("1. Agregar canción")
        print("2. Eliminar canción")
        print("3. Reproducir siguiente")
        print("4. Reproducir anterior")
        print("5. Mostrar canción actual")
        print("6. Mostrar lista de canciones")
        print("7. Buscar canción")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la canción: ")
            try:
                duracion = int(input("Duración (en segundos): "))
                canciones.agregar_cancion(nombre, duracion)
            except ValueError:
                print("Error: La duración debe ser un número entero.")
        elif opcion == "2":
            nombre = input("Nombre de la canción a eliminar: ")
            canciones.eliminar_cancion(nombre)
        elif opcion == "3":
            canciones.siguiente_cancion()
        elif opcion == "4":
            canciones.cancion_anterior()
        elif opcion == "5":
            canciones.mostrar_actual()
        elif opcion == "6":
            canciones.mostrar_lista()
        elif opcion == "7":
            nombre = input("Nombre de la canción a buscar: ")
            canciones.buscar_cancion(nombre)
        elif opcion == "0":
            print("Cerrando reproductor...")
            salir = True
        else:
            print("Opción no válida. Intenta de nuevo.")
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
    def __init__(self):
        self.primera_cancion = None 
        self.ultima_cancion = None  
        self.cancion_actual = None  
        self.size = 0

    def vacia(self):
        return self.primera_cancion is None

    # --- FUNCIONES DE UN SOLO PASO (Sin recursividad) ---
    def agregar_cancion(self, nom, seg):
        nuevo_nodo = Node(nom, seg)
        if self.vacia():
            self.primera_cancion = self.ultima_cancion = nuevo_nodo
        else:
            self.ultima_cancion.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultima_cancion
            self.ultima_cancion = nuevo_nodo
        self.size += 1
        print(f"Canción agregada: {nom}")

    def siguiente_cancion(self):
        if self.vacia():
            print("La lista está vacía.")
        elif self.cancion_actual is None:
            self.cancion_actual = self.primera_cancion
            print("Reproduciendo: ", self.cancion_actual.nom)
        elif self.cancion_actual.siguiente is None:
            print("Estás en la última canción. No hay más adelante.")
        else:
            self.cancion_actual = self.cancion_actual.siguiente
            print("Reproduciendo: ", self.cancion_actual.nom)

    def mostrar_actual(self):
        if self.cancion_actual is None:
            print("No hay ninguna canción reproduciéndose en este momento.")
        else:
            print(f"Canción actual: {self.cancion_actual.nom} | Duración: {self.cancion_actual.seg}s")

    def cancion_anterior(self):
        if self.vacia():
            print("La lista está vacía.")
        elif self.cancion_actual is None or self.cancion_actual.anterior is None:
            print("No hay canciones atrás. Estás al principio de la lista.")
        else:
            self.cancion_actual = self.cancion_actual.anterior
            print("Reproduciendo: ", self.cancion_actual.nom)

    # --- FUNCIONES RECURSIVAS ---

    # Mostrar lista recursivo
    def mostrar_lista(self, nodo=None, inicial=True, posicion=1):
        if self.vacia():
            print("La lista está vacía.")
            return

        # Configuración de la primera llamada
        if inicial:
            print("\n--- Lista de Reproducción ---")
            nodo = self.primera_cancion

        # CASO BASE: Si llegamos al final de la lista, detenemos la recursividad
        if nodo is None:
            print("-----------------------------\n")
            return

        # Mostrar el nodo actual
        estado = " (Sonando)" if nodo == self.cancion_actual else ""
        print(f"{posicion}. {nodo.nom} - {nodo.seg}s{estado}")

        # LLAMADA RECURSIVA: Pasamos al siguiente nodo
        self.mostrar_lista(nodo.siguiente, False, posicion + 1)


    # Buscar canción recursivo
    def buscar_cancion(self, nom, nodo=None, inicial=True):
        if self.vacia():
            print("La lista está vacía.")
            return

        if inicial:
            nodo = self.primera_cancion

        # CASO BASE 1: Llegamos al final sin encontrarla
        if nodo is None:
            print("Canción no encontrada:", nom)
            return

        # CASO BASE 2: Encontramos la canción
        if nodo.nom == nom:
            print(f"Encontrada: '{nom}' | Duración: {nodo.seg} segundos.")
            return

        # LLAMADA RECURSIVA
        self.buscar_cancion(nom, nodo.siguiente, False)


    # Eliminar canción recursivo
    def eliminar_cancion(self, nom, nodo=None, inicial=True):
        if self.vacia():
            if inicial: print("La lista está vacía.")
            return

        if inicial:
            nodo = self.primera_cancion

        # CASO BASE 1: No se encontró la canción
        if nodo is None:
            print("Canción no encontrada:", nom)
            return

        # CASO BASE 2: Encontramos el nodo a eliminar
        if nodo.nom == nom:
            if nodo == self.cancion_actual:
                self.cancion_actual = None
                print("Se detuvo la reproducción porque la canción fue eliminada.")

            # Reconectar el nodo anterior (si existe)
            if nodo.anterior is not None:
                nodo.anterior.siguiente = nodo.siguiente
            else:
                self.primera_cancion = nodo.siguiente

            # Reconectar el nodo siguiente (si existe)
            if nodo.siguiente is not None:
                nodo.siguiente.anterior = nodo.anterior
            else:
                self.ultima_cancion = nodo.anterior

            self.size -= 1
            print("Canción eliminada exitosamente:", nom)
            return

        # LLAMADA RECURSIVA
        self.eliminar_cancion(nom, nodo.siguiente, False)


# Menú principal
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
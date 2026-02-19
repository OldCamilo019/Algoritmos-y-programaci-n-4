#hacer una menu en terminal que haga listas de canciones a la lista cuando las agrego saber la duracion
#poder pasar de canciones
#saber que cancion estoy escuchando
#eliminar canciones
#buscar canciones
#me muestre la lista de las canciones
# cual esta sonando en ese momento

from asyncio.windows_events import NULL
from gettext import NullTranslations


class NodoDoble:
	#Nodo para lista simplemente enlazada

	def __init__(self,dato, segundos):
		self.dato = dato
		self.segundos = segundos

		self.siguiente = None
		self.anterior = None
		self.reproductor = None

class ListaDoble:
	#Lista doblemente enlazada

	def __init__(self):
		self.cabeza = None
		self.cola = None

	def esta_vacia(self):
		#verifica si la lista esta esta_vacia

		return self.cabeza is None

	def insertar_inicio(self, dato, segundos):
		#Inserta un elemento al inicio de la lista
		nuevo = NodoDoble(dato, segundos) 

		if self.esta_vacia():
			self.cabeza = nuevo
			self.cola = nuevo
			self.reproductor = nuevo
		else:
			nuevo.siguiente = self.cabeza
			self.cabeza.anterior = nuevo
			self.cabeza = nuevo

	def insertar_final(self, dato, segundos):
		#Inserta un elemento al inicio de la lista
		nuevo = NodoDoble(dato,segundos) 

		if self.esta_vacia():
			self.cabeza = nuevo
			self.cola = nuevo
		else:
			self.cola.siguiente = nuevo
			nuevo.anterior = self.cola
			self.cola = nuevo

	def eliminar_inicio(self):
		#elimina el primer elemento de la lista

		if self.esta_vacia():
			return None

		dato = self.cabeza.dato

		if self.cabeza == self.cola:
			#solo un elemento
			self.cabeza = None
			self.cola = None
		else:
			self.cabeza = self.cabeza.siguiente
			self.cabeza.anterior = None

		return dato #opcional

	def eliminar_final(self):
		#elimina el primer elemento de la lista

		if self.esta_vacia():
			return None

		dato = self.cola.dato

		if self.cabeza == self.cola:
			#solo un elemento
			self.cabeza = None
			self.cola = None
		else:
			self.cola = self.cola.anterior
			self.cola.siguiente = None

		return dato #opcional

	def recorrer_adelante(self):
		#Imprime listade inicio a fin

		if self.esta_vacia():
			print("Lista Vacia")
			return

		print("Inicio -> Fin:", end=" ")
		actual = self.cabeza
		elementos = []
		while actual:
			elementos.append(str(actual.dato))
			actual = actual.siguiente
		print (" <->".join(elementos))

	def recorrer_atras(self):
		#Imprime listade fin al inicio

		if self.esta_vacia():
			print("Lista Vacia")
			return

		print("Fin -> Inicio:", end=" ")
		actual = self.cola
		elementos = []
		while actual:
			elementos.append(str(actual.dato))
			actual = actual.anterior
		print (" <->".join(elementos))

	def buscar(self, dato, segundos):
		#busca un elemento en la lista
		actual = self.cabeza
		while actual:
			if actual.dato == dato:
				return True
			actual = actual.siguiente
		return False

	def __len__(self): # se una __len__ para invocarlo como len(lista) en vez de lista.contar
		#Retorna la cantidad de elementos
		contador = 0
		actual = self.cabeza
		while actual:
			contador += 1
			actual = actual.siguiente
		return contador

	def __str__(self):
		#Representacion de la lista devuelve print(lista)
		if self.esta_vacia():
			return "Lista de reproduccion Vacia"

		elementos = []
		actual = self.cabeza
		while actual:
			elementos.append(str(actual.dato))
			actual = actual.siguiente
		return " <-> ".join(elementos)


	def Cancion_Siguiente_O_Anterior(self):
		if self.esta_vacia():
			return "Lista de reproduccion Vacia"

		actual= self.reproductor

		self.reproductor=actual.siguiente

#Interfaz

def Esta_Sonando(cancion):
	print("==================================")
	print("Estas escuchando:", cancion)
	print("<- (9) Cancion Anterior | (0) Cancion siguiente ->")
	print("==================================")


def Menu_Principal():
	print("Reproductor")
	print("1) Agregar Cancion    | 2)Mostrar la lista  | 3)Repoducir la lista")
	print("4) Buscar en la lista | 5) Eliminar Cancion | 6) Salir")




if __name__ == "__main__": #opcional

	salir = 0 
	canciones = ListaDoble()


	while salir == 0:
		Menu_Principal()
		
		opcion = int(input("Ingrese su opcion:"))


		if opcion == 1:			
			cancion = input("Ingrese el nombre de la cancion:")
			segundos = input("Ingrese los segundos de la cancion:")
			canciones.insertar_final(cancion, segundos)

		elif opcion == 2:
			print(canciones)	

		elif opcion == 5:
			cancion=input("Ingrese el nombre de la cancion que desea eliminar:")
			canciones.eliminar_inicio()
			canciones.buscar()
			canciones.eliminar_final()		
			
	
class NodoDoble:
	#Nodo para lista simplemente enlazada

	def __init__(self,dato):
		self.dato = dato
		self.siguiente = None
		self.anterior = None

class ListaDoble:
	#Lista doblemente enlazada

	def __init__(self):
		self.cabeza = None
		self.cola = None

	def esta_vacia(self):
		#verifica si la lista esta esta_vacia

		return self.cabeza is None

	def insertar_inicio(self, dato):
		#Inserta un elemento al inicio de la lista
		nuevo = NodoDoble(dato) 

		if self.esta_vacia():
			self.cabeza = nuevo
			self.cola = nuevo
		else:
			nuevo.siguiente = self.cabeza
			self.cabeza.anterior = nuevo
			self.cabeza = nuevo

	def insertar_final(self, dato):
		#Inserta un elemento al inicio de la lista
		nuevo = NodoDoble(dato) 

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
			self.cabeza.anterior = none

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

	def buscar(self, dato):
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
			return "Lista Vacia"

		elementos = []
		actual = self.cabeza
		while actual:
			elementos.append(str(actual.dato))
			actual = actual.siguiente
		return " <-> ".join(elementos)
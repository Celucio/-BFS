'''
Autor: Carlos Lucio
Para comenzar con la generación de los métodos de busqueda necesitaremos de las librerias necesarias
En python los metodos de busqueda se puede asociar con la teoria de Grafos.
Es por ello que para crear la clase Grafos
Importaremos la libreria Queue para generar listas en el programa
'''
#Importamos la libreria Queue
from queue import Queue

#Crearemos una clase grafo para instanciar el objeto y generar nodos
class Grafo():
    # Constructor
    def __init__(self, numero_de_nodos, dirigido=True):
        '''
        Por medio de parámetros de entrada recibe el nodo
        '''
        #Definiendo las variables del constructor del grafo
        self.m_numero_de_nodos = numero_de_nodos 
        '''
        Esta variable determinar el rango de nodos que tendra el grafo
        enviando como parámetro la variable generada nodo.matriz_numero_de_nodos
        '''
        #Mide el rango de nodos
        self.m_nodos = range(self.m_numero_de_nodos) 
		
        #Dirigido o No Dirigido
        self.m_dirigido = dirigido
        #Representación del grafo - Lista de Adyacencia
        self.m_adyacencia_lista = {self: set() for self in self.m_nodos}     
        
    #Añade un nodo al grafo
    def añadir_nodo(self, nodo1, nodo2, peso=1):
        '''
        Funcion que recibe por parámetro los nodos
        retorna la agregación de los nodos en la lista
        '''
        #Ingreso del nodo2 a la lista de adyacencia del nodo1
        self.m_adyacencia_lista[nodo1].add((nodo2, peso))
        #Estructura condicional en caso de que no sea dirigido
        if not self.m_dirigido: 
            #Ingreso del nodo1 a la lista de adyacencia del nodo2
            self.m_adyacencia_lista[nodo2].add((nodo1, peso)) #Añadir el nodo1 a la lista de adyacencia del nodo2



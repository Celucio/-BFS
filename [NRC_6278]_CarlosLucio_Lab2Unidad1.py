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




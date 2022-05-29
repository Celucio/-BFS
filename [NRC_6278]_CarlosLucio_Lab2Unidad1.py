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

    # Imprime la representación del grafo
    def mostrar_lista_adyacencia(self):
        '''
        Recorrido de la lista por parte de una clave
        Retorna la impresión del nodo y el grafo
        '''
        #Generacion del ciclo for que permite recorrer el tamaño del nodo
        for clave in self.m_adyacencia_lista.keys(): 
            #Muestra en la terminal el grafo
            print("Nodo", clave, ": ", self.m_adyacencia_lista[clave]) 
    #Función que imprime el recorrido BFS desde un vértice fuente dado. bfs_traversal(int s) recorre los vértices alcanzables desde s.
    def bfs_transversal(self, nodo_inicial):
        '''
        Recibe el valor de nodo_inicial, genera una lista de las colas visitadas 
        y muestra el recorrido  realizado. 
        '''
        #Creación de nodos visitados
        visitado = set()
        #Definición de un elemento de tipo lista
        cola = Queue()

        #Añade el nodo a la lista
        cola.put(nodo_inicial)
        #Añade el nodo a la lista visitada
        visitado.add(nodo_inicial)
        #Bucle que permite mostrar los nodos
        while not cola.empty():
            #Quitar un vértice de la cola
            nodo_actual = cola.get()
            #Imprimir el nodo siguiente
            print(nodo_actual, end = " ")
            #Ciclo que obtiene todos los vértices adyacentes del vértice eliminado
            for (nodo_proximo, peso) in self.m_adyacencia_lista[nodo_actual]:
                
                #Nodo no visitado
                if nodo_proximo not in visitado:
                    '''
                    Estructura condicional:
                    Si un nodo adyacente no es visitado
                    Indique al nodo como visitado y añada a la lista
                    '''
                    #Añade el nodo a la cola
                    cola.put(nodo_proximo)
                    #Indica que el nodo ha sido visitado
                    visitado.add(nodo_proximo)

#Main
if __name__ == "__main__":
    #Instanciamos el objeto
    g = Grafo(5, dirigido=False)

    #Agregue bordes al grafo con peso predeterminado = 1
    g.añadir_nodo(0, 1)
    g.añadir_nodo(0, 2)
    g.añadir_nodo(1, 2)
    g.añadir_nodo(1, 4)
    g.añadir_nodo(2, 3)

    #Imprime el grafo generado en el formulario nodo n: {(nodo, peso)}
    g.mostrar_lista_adyacencia()

    #Muestra por medio de una lista las colas visitadas
    print ("A continuación se muestra el recorrido primero en anchura (a partir del vértice 0)")
    #Retorno de las colas visitadas 
    g.bfs_transversal(0)

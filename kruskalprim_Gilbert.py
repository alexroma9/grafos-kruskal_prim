from grafo import Grafo
import random

def gilbert(n, pr):
  """
  Grafo Gilbert (Método aleatorio)
  n : número de nodos
  pr : probabilidad asignada que se considerá para generar si / no la arista entre dos nodos.
  """
  g = Grafo('Gilbert')
  for i in range(n):
    g.addNodo(str(i))

  Aristas = 1
  for i in range(n):
    for j in range(n):
      if random.random() < pr:
        if (j != i):
            peso = random.randint(1, 50)
            g.addArista('{} -- {}'.format(str(i),str(j)),str(i),str(j),peso)
            Aristas += 1
  return g
 
print ("Modelo Gilbert  ----------")
nodo = int(input("Ingrese número de nodos: "))
prob = float(input("Ingrese la probabilidad de crear la arista: "))
nodo_fin = int(input("Indica el segundo nodo o final a encontrar ruta : "))

gilbert_ = gilbert(nodo,prob)
gilbert_.savedArchivoDijsktra('{}_n{}'.format('_completo',str(nodo)))

n_inicia = list(gilbert_.nodos.keys())[0]
n_final = list(gilbert_.nodos.keys())[nodo_fin]


grafoKruskal = Grafo.KruskalID(gilbert_,n_inicia,n_final)
grafoKruskal.generarArchivoGVKruskal('{}_n{}'.format('_Gilbert',str(nodo)))

grafoKruskalInverso = Grafo.KruskalInverso(gilbert_,n_inicia,n_final)
grafoKruskalInverso.generarArchivoGVKruskal('{}_n{}'.format('_Gilbert',str(nodo)))

grafoPrim = Grafo.Prim(gilbert_,n_inicia,n_final)
grafoPrim.generarArchivoGVKruskal('{}_n{}'.format('_Gilbert',str(nodo)))



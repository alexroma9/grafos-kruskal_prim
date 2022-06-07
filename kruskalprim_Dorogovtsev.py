from grafo import Grafo
import random

def dorogovtsev_mendes(n, directed=False):
    """
    Grafo Dorogovtsev (Método aleatorio)
    n : número de nodos.
    """
    g = Grafo('Dorogovtse')
    g.addArista('0 -- 1', str(0), str(1))
    g.addArista('0 -- 2', str(0), str(2))
    g.addArista('1 -- 2', str(1), str(2))
    for nAdic in range(3, n-2):
        num_edges = len(g.aristas)
        random_edges = random.randint(1,num_edges-1)
        list_edge = list(g.aristas.keys())
        edges_select = list_edge[random_edges]
        nI = g.aristas[edges_select].inicio.id
        nF = g.aristas[edges_select].final.id
        peso = random.randint(1, 50)
        peso2 = random.randint(1, 50)

        g.addArista('{} -- {}'.format(str(nAdic), str(nI)), str(nAdic), str(nI),peso)
        g.addArista(str('{} -- {}'.format(str(nAdic), str(nF))), str(nAdic), str(nF),peso2)

    return g


print ("Modelo Dorogovtsev  ----------")
nodo = int(input("Ingrese número de nodos: "))
nodo_fin = int(input("Indica el segundo nodo o final a encontrar ruta : "))

dorogovtsev_mendes_ = dorogovtsev_mendes(nodo)
dorogovtsev_mendes_.savedArchivoDijsktra('{}_n{}'.format('_completo',str(nodo)))

n_inicia = list(dorogovtsev_mendes_.nodos.keys())[0]
n_final = list(dorogovtsev_mendes_.nodos.keys())[nodo_fin]

grafoKruskal = Grafo.KruskalID(dorogovtsev_mendes_,n_inicia,n_final)
grafoKruskal.generarArchivoGVKruskal('{}_n{}'.format('_Dorogovtsev',str(nodo)))

grafoKruskalInverso = Grafo.KruskalInverso(dorogovtsev_mendes_,n_inicia,n_final)
grafoKruskalInverso.generarArchivoGVKruskal('{}_n{}'.format('_Dorogovtsev',str(nodo)))

grafoPrim = Grafo.Prim(dorogovtsev_mendes_,n_inicia,n_final)
grafoPrim.generarArchivoGVKruskal('{}_n{}'.format('_Dorogovtsev',str(nodo)))


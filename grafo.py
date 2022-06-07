#from grafo import Grafo
from nodo import Nodo 
from arista import Arista 
neighbour = 'Vecino'
edge = 'Arista'
dijkstra = 'Dijkstra'


class Grafo():
  """
  Clase Grafo
  """
  def __init__(self, nombre):
    """
    Inicializa el grafo.
    nombre : Nombre del grafo.
    nodos
    aristas
    """
    self.id = nombre
    self.nodos = {} 
    self.aristas = {}
  
  def savedArchivo(self):
    """
    Guarda datos de grafo en formato .gv
    Warning : Cuidado ya que sobre escribe una vez ejecutado el grafo solicitado.
    """
    file = open('{}.gv'.format(self.id), 'w')
    file.write('digraph #nombre {' + '\n')
    for arista in self.aristas:
      objetoArista = self.aristas[arista]
      nodoInicial = objetoArista.inicio.id
      nodoFinal = objetoArista.final.id
      #file.write('{};'.format(arista) + '\n')a
      file.write('{} -- {};'.format(nodoInicial,nodoFinal) + '\n')
    file.write('}')
    file.close()

  def savedArchivoDijsktra(self, sufijo):
    """
    Guarda datos de grafo en formato .gv 
    Para Dijkstra
    """
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
#    nodo = self.nodos
#    print (nodo)
    for arista in self.aristas:
      file.write('{};'.format(arista) + '\n')
#      file.write('{} [label="{}"]'.format(arista,self.nodos[nodo].attributos['Dijkstra']) + '\n')
#      nodo = nodo + 1

    for nodo in self.nodos:
      file.write('{} [label="{}"]'.format(nodo,self.nodos[nodo].attributos['Dijkstra']) + '\n')
    file.write('}')
    file.close()

  def generarArchivoGVKruskal(self, sufijo):
    file = open('{}{}.gv'.format(self.id, sufijo), 'w')
    file.write('graph #nombre {' + '\n')
    pesoFinal = 0
    for arista in self.aristas:
      peso = self.aristas[arista].atributos["Peso"]
      pesoFinal += int(peso)
      file.write('{} [label={}]'.format(arista, self.aristas[arista].atributos["Peso"]) + '\n')
    file.write(str(pesoFinal) + '\n')
    file.write('}')
    file.close()  

  def addNodo(self, nombreNodo):
    """
    Crea nodo , si esta creado no hace nada de lo contrario crea.
    """
    if nombreNodo in self.nodos:
        pass
    else:
      _nodo = Nodo(nombreNodo)
      self.nodos[nombreNodo] = _nodo
    return self.nodos[nombreNodo]
  
  def addArista(self, nombreArista, nombreNodoOrigin, nombreNodoDestino, peso=0):
    """
    Crea arista, si esta creada no hace nada, de lo contrario crea.
    """
    #if nombreArista in self.aristas:
    #    pass
    #else:
    arista_ = self.aristas.get(nombreArista)

    if arista_ is None:
        nodoOrigen = self.addNodo(nombreNodoOrigin)
        nodoDestino = self.addNodo(nombreNodoDestino)
        #_arista = Arista(nombreArista,self.nodos[nombreNodoOrigin],self.nodos[nombreNodoDestino],peso)
        _arista = Arista(nombreArista,nodoOrigen,nodoDestino,peso)
        self.aristas[nombreArista] = _arista
        nodoOrigen.attributos[neighbour].append(nodoDestino)
        nodoDestino.attributos[neighbour].append(nodoOrigen)
        nodoOrigen.attributos[edge].append(_arista)
        nodoDestino.attributos[edge].append(_arista)

  def giveNodo(self, nombre):
    return self.nodos[nombre]
  
  def givedegreesNodo(self, nombreNodo):
    """
    Entrega el grado del nodo considerado.
    """
    if not nombreNodo in self.nodos:
      print('Nodo no existe')

    else:
      _nodo = self.nodos[nombreNodo]
      grado = len(_nodo.attributos[neighbour])
      return grado
  
  def bfs(grafoGenerado, s):
      """
      BFS
      : parametro s : nodo fuente o root
      : g grafo generado por BFS
      """
      gbfs = Grafo('BFS')
      visitado = [s]
      cola = [s]
      diccionarioNodos = grafoGenerado.nodos
      while cola:
          m = cola.pop(0)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitado:
                  visitado.append(nodoAdjacente.id)
                  cola.append(nodoAdjacente.id)
                  gbfs.addArista('{} -- {}'.format(str(m), str(nodoAdjacente.id)),str(m),str(nodoAdjacente.id))     
      return gbfs

  def dfsr(grafoGenerado, nodoFuente, visitados, grafoDFSR):
      diccionarioNodos = grafoGenerado.nodos
      visitados.append(nodoFuente)
      for nodoAdjacente in diccionarioNodos[nodoFuente].attributos['Vecino']:
          if nodoAdjacente.id not in visitados:
              grafoDFSR.addArista('{} -- {}'.format(str(nodoFuente), str(nodoAdjacente.id)),str(nodoFuente),str(nodoAdjacente.id))     
              visitados,grafoDFSR = Grafo.dfsr(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
              #grafoDFSR = DFSR(grafoGenerado, nodoAdjacente.id, visitados, grafoDFSR)
      return visitados,grafoDFSR


  def dfsi(grafoGenerado, nodoFuente):
      """
      Funcion para generar un arbol DFS dado un grafo : grafoGenerado
      y un nodo inicio : nodoFuente
      Utilizamos el array visitados por que nodos hemos pasado
      DFS utiliza una pila para recorrer el grafo Last in First Out
      """

      gdfsi = Grafo('DFSi')
      diccionarioNodos = grafoGenerado.nodos 
      visitados = [nodoFuente]
      pila = [nodoFuente]
      while pila:
          m = pila.pop()
          if m not in visitados:
              visitados.append(m)
          for nodoAdjacente in diccionarioNodos[m].attributos['Vecino']:
              if nodoAdjacente.id not in visitados:
                  if nodoAdjacente.id not in pila:
                      pila.append(nodoAdjacente.id)

          if pila:
              ultimoNodo = pila[-1]
              gdfsi.addArista('{} -- {}'.format(str(m), str(ultimoNodo)),str(m),str(ultimoNodo))

      return gdfsi


  def dijkstra(grafoFuente, s, t):
      """
      dijkstra encuentra camino más corto entre nodos en un grafo.
      :param grafoFuente: el grafo original
      :param s: node fuente
      :param t: node objetivo
      :return g un grafo del nodo fuente al nodo objetivo
      """
      l = []
      dist = {}
      prev = {}
      descubierto = {}
      diccNodos = grafoFuente.nodos
      diccAristas = grafoFuente.aristas
      for v in diccNodos:
          dist[v] = float('inf')
          prev[v] = None
          descubierto[v] = False
      dist[s] = 0
      l.append((s, dist[s]))
      while len(l) != 0:
          u = min(l, key=lambda x: x[1])
          l.remove(u)
          u = u[0]
          descubierto[u] = True
          if u == t:
              break
          for v in diccNodos[u].attributos['Vecino']:
              if not descubierto[v.id]:
                  try:
                      alt = dist[u] + diccAristas['{} -- {}'.format(u,v.id)].attributos["Peso"]
                  except:
                      alt = dist[u] + diccAristas['{} -- {}'.format(v.id,u)].attributos["Peso"]
                  if alt < dist[v.id]:
                      dist[v.id] = alt
                      prev[v.id] = u
                      l.append((v.id, dist[v.id]))

      u = t
      g = Grafo('Dijkstra')
      while u is not None:
          nodoU = g.addNodo(u)
          nodoU.attributos['Dijkstra'] = dist[u]
          if prev[u] is not None:
              nodoPrevioU = g.addNodo(prev[u])
              nodoPrevioU.attributos['Dijkstra'] = dist[prev[u]]
              g.addArista('{} -- {}'.format(prev[u],u),prev[u],u)
              u = prev[u]
          else:
              break
      return g


   def KruskalInverso(grafoFuente):
       g = clone(grafoFuente)
       q = sorted(grafoFuente.aristas.items(), key=lambda e: e[1].atributos["Peso"],reverse=True)
       for e in q:
           g2 = clone(g)
           g2.aristas.pop(e[0])
           arbolBFS = BFS(g2,'0')

            if len(g2.nodos) != len(arbolBFS.nodos):
              g2 = clone(g)
            else:
              nombreArista = e[0]
              nombreNodoOrigen = e[1].n0.id
              nombreNodoDestino = e[1].n1.id
              peso = e[1].atributos['Peso']
              g.agregarArista(nombreArista,nombreNodoOrigen,nombreNodoDestino,peso)
        return g



  def clone(grafoCopiar):
      id = grafoCopiar.id
      nodos = grafoCopiar.nodos.copy()
      aristas = grafoCopiar.aristas.copy()

      g = Grafo()
      g.id = id
      g.nodos = nodos
      g.aristas = aristas

    return g

  def KruskalD(grafoFuente):

        g = Grafo()

        # Create set for each v of V[G]
        parent = []
        rank = []
        diccionarioNodos = grafoFuente.nodos
        diccionarioAristas = grafoFuente.aristas
        for v in diccionarioNodos:
            parent.append(v)
            rank.append(0)

        # Sort edges by weight
        q = sorted(diccionarioAristas.items(), key=lambda e: e[1].atributos["Peso"])
        for e in q:
          u = e[1].n0.id
          v = e[1].n1.id

          v1 = encuentraConjunto(parent, u)
          v2 = encuentraConjunto(parent, v)
          if v1 != v2:
            g.agregarArista('{} -- {}'.format(str(u), str(v)),str(u),str(v), e[1].atributos["Peso"])

            if rank[int(v1)] < rank[int(v2)]:
              parent[int(v1)] = v2
              rank[int(v2)] += 1
            else:
              parent[int(v2)] = v1
              rank[int(v1)] += 1

        return g



  def encuentraConjunto(fuente, i):
      if fuente[int(i)] == i:
      return i

      return encuentraConjunto(fuente, fuente[int(i)])

  def Prim(grafoFuente):

        g = Grafo()
        diccionarioNodos = grafoFuente.nodos
        diccionarioAristas = grafoFuente.aristas

        distance = [sys.maxsize] * len(diccionarioNodos)
        parent = [None] * len(diccionarioNodos)
        set = [False] * len(diccionarioNodos)

        distance[0] = 0

        for i in diccionarioNodos:
            min_index = 0
            min = sys.maxsize
            for v in diccionarioNodos:
                if distance[int(v)] < min and set[int(v)] is False:
                    min = distance[int(v)]
                    min_index = int(v)
            u = min_index

            set[u] = True
            g.agregarNodo(u)

            for v in diccionarioNodos[str(u)].atributos["Vecinos"]:
                try:
                    if set[int(v.id)] is False and distance[int(v.id)] > diccionarioAristas['{} -- {}'.format(str(u), str(v.id))].atributos["Peso"]:
                      distance[int(v.id)] = diccionarioAristas['{} -- {}'.format(str(u), str(v.id))].atributos["Peso"]
                      parent[int(v.id)] = u

                except:
                  if set[int(v.id)] is False and distance[int(v.id)] > diccionarioAristas['{} -- {}'.format(str(v.id), str(u))].atributos["Peso"]:
                      distance[int(v.id)] = diccionarioAristas['{} -- {}'.format(str(v.id), str(u))].atributos["Peso"]
                      parent[int(v.id)] = u

        for i in diccionarioNodos:
            if i == 0:
                continue
            if parent[int(i)] is not None:
              try:
                  g.agregarArista('{} -- {}'.format(str(parent[int(i)]), str(i)),str(parent[int(i)]),str(i), diccionarioAristas['{} -- {}'.format(str(parent[int(i)]), str(i))].atributos["Peso"])
              except:
                 g.agregarArista('{} -- {}'.format(str(parent[int(i)]), str(i)),str(parent[int(i)]),str(i), diccionarioAristas['{} -- {}'.format(str(i),str(parent[int(i)]))].atributos["Peso"])
        return g

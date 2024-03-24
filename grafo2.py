from math import inf
import re

class Grafo:
  def __init__(self, V = [], E = [], w = {}) -> None:
    self.V = V
    self.E = E
    self.w = w

  def __str__(self) -> str:
    return f"Graph(V={self.V}, E={self.E}, w={self.w})"
  
  def qtdVertices(self):
    return len(self.V)
  
  def qtdArestas(self):
    return len(self.E)
  
  def grau(self, v):
    """ Definição: Arestas entrantes no vértice v
        ### Corrigido
    """
    return len([vizinho for vizinho in self.E if v in vizinho])
  
  def rotulo(self, v):
    """ Definição: Nome do vértice
        ### Corrigido
    """
    return self.V[v][1]
  
  def vizinhos(self, v):
    """ Definição: Vizinhos do vértice v
        ### Corrigido
    """
    arestas_vizinhos_v = [vizinho for vizinho in self.E if v in vizinho]
    vizinhos = []
    for aresta in arestas_vizinhos_v:
      a, b = aresta[0], aresta[1]
      if a == v:
        vizinhos.append(b)
      else:
        vizinhos.append(a)
    
    return [vertice for vertice in self.V if vertice[0] in vizinhos]
  
  def haAresta(self, u, v):
    """
        ### Corrigido
    """
    return (u in self.E[v]) or (v in self.E[u])
  
  def peso(self, u, v):
    """
        ### Corrigido
    """
    if not ( (u, v) in self.w or (v, u) in self.w ):
        return inf
    return self.w[(u, v)] if (u, v) in self.w else self.w[(v, u)]

  def ler(self, nomeArquivo):
    with open(nomeArquivo, "r") as f:
      lines = f.readlines()
      current_read = ""

      for line in lines:
        if line.startswith("*vertices"):
          current_read = "vertices"
          continue
        elif line.startswith("*edges"):
          current_read = "edges"
          continue
  
        if current_read == "vertices":
          name = line.split('"')[1]
          id = line.split()[0]
          self.V.append((id, name))
          
        if current_read == "edges":
          u, v, w = line.split()
          u, v, w = int(u), int(v), float(w)
          self.E.append((u, v))
          self.w[(u, v)] = w
          
      return self
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
        ### TODO: Corrigir: Está retornando valor errado
    """
    return len(self.E[v])
  
  def rotulo(self, v):
    """ Definição: Nome do vértice
        ### TODO: Corrigir: Retornar apenas o rótulo (nome) do vértice
    """
    return self.V[v]
  
  def vizinhos(self, v):
    """ Definição: Vizinhos do vértice v
        ### TODO: Corrigir
    """
    return self.E[v]
  
  def haAresta(self, u, v):
    """ Retorna:
        True - Existe a aresta u -> v ou v -> u
        False - Não existe a aresta u -> v ou v ->
        ### TODO: Corrigir
    """
    return u in self.E[v]
  
  def peso(self, u, v):
    """
        ### TODO: Corrigir (0, 3) == (3,0)
    """
    return self.w[(u, v)] if (u, v) in self.w else inf

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
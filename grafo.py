from math import inf
import os

class Grafo:
  def __init__(self, V = [], E = [], w = {}) -> None:
    self.V = V # Vertices
    self.E = E # Arestas
    self.w = w # Pesos das Arestas

  def __str__(self) -> str:
    return f"Vertices: {self.V}\n\nArestas: {self.w}"

  def __repr__(self):
    return f"Graph(V={self.V}, E={self.E}, w={self.w})"

  def qtdVertices(self):
    return len(self.V)
  
  def qtdArestas(self):
    return len(self.E)
  
  def grau(self, v):
    return len([vizinho for vizinho in self.E if v in vizinho])
  
  def rotulo(self, v):
    return self.V[v][1]
  
  def vizinhos(self, v):
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
    return (u in self.E[v]) or (v in self.E[u])

  def haIndice(self, i: str) -> bool:
    return any(v[0] == i for v in self.V)

  def peso(self, u, v):
    if not ( (u, v) in self.w or (v, u) in self.w ):
        return inf
    return self.w[(u, v)] if (u, v) in self.w else self.w[(v, u)]

  def ler(self, nome_arquivo):
    if not os.path.exists(nome_arquivo):
      print(f"\n> Arquivo {nome_arquivo} não encontrado\n")
      return None
  
    with open(nome_arquivo, "r") as f:
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

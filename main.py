from grafo import Grafo

def main():
  V = [(0, "A"), (1, "B"), (2, "C"), (3, "D"), (4, "E")]
  E = [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (0, 4)]
  w = { (0, 1): 1, (1, 2): 2, (2, 3): 3, (3, 0): 4 }
  G = Grafo(V, E, w)
  # print(G)
  # print(G.qtdVertices())
  # print(G.qtdArestas())
  # print(G.grau(0))
  # print(G.rotulo(0))
  # print(G.vizinhos(0))
  # print(G.haAresta(1, 0))
  # print(G.haAresta(0, 2))
  print(G.peso(1, 0))
  print(G.peso(0, 2))
  print(G.peso(0, 3))
  G2 = Grafo()
  # print(G2.ler("facebook_santiago.net"))
  
if __name__ == "__main__":
  main()
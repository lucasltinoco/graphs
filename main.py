from graph import Graph

def main():
  V = [0, 1, 2, 3]
  E = [(0, 1), (1, 2), (2, 3), (3, 0)]
  w = { (0, 1): 1, (1, 2): 2, (2, 3): 3, (3, 0): 4 }
  G = Graph(V, E, w)
  print(G)
  
if __name__ == "__main__":
  main()
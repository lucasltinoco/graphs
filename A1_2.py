"""
BFS - BREADTH-FIRST SEARCH ALGORITHM

Algoritmo criado para realizar busca em largura em um grafo.

Uso: python A1_2.py graph_filename graph_index

args: 
    graph: Grafo()
    s: indice do vertice inicial
"""
from A1_1 import Grafo
import sys, os
from math import inf
from queue import Queue
import pandas as pd

def bfs(graph: Grafo, s: int):
    C = [] # Conhecido
    D = [] # Distancia
    A = [] # Ancestral
    
    for i in range(graph.qtdVertices() + 1):
        C.append(False)
        D.append(inf)
        A.append(None)

    C[s] = True
    D[s] = 0
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        current_node = Q.get() # Retiro o vertice da queue
        print("\n\n> Visitando vertice:",current_node)

        for vizinho in graph.vizinhos(current_node):
            if not C[vizinho]:
                C[vizinho] = True
                D[vizinho] = D[current_node] + 1
                A[vizinho] = current_node
                Q.put(vizinho)
                print("- Conhecendo vertice:", vizinho)
    
    df = pd.DataFrame({'Conhecidos': C[1::], 'Distancias': D[1::], 'Ancestrais': A[1::]}, index=range(1, len(C)))
    print('\n',df)
    return (D, A)



if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('\n> Uso: python A1_2.py graph_filename graph_index\n')
        sys.exit(1)

    graph_filename = sys.argv[1]
    graph_index = int(sys.argv[2])

    # Verifica se o nome do arquivo passado existe
    if not os.path.exists(graph_filename):
        print(f"\n> graph_filename: {graph_filename} não existe\n")
        sys.exit(1)

    try:
        grafo = Grafo() # Inicializa o grafo vazio
        grafo.ler(graph_filename) # Adiciona elementos ao grafo
    except Exception as e:
        print(f"\n> Erro ao incializar o grafo: {e}\n")
        sys.exit(1)

    # Verifica se o indice passado existe no grafo
    if not grafo.haIndice(graph_index):
        print(f"\n graph_index não existe no grafo selecionado\n")
        sys.exit(1)

    # Executa a busca em largura
    resultado = bfs(grafo, graph_index)


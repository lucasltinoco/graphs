"""
BFS - BREADTH-FIRST SEARCH ALGORITHM

Algoritmo criado para realizar busca em largura em um grafo.

Uso: python bfs.py graph_filename graph_index

args: 
    graph: Grafo()
    s: indice do vertice inicial
"""
from grafo import Grafo
import sys, os

def bfs(graph: Grafo, s: int):
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('\n> Uso: python bfs.py graph_filename graph_index\n')
        sys.exit(1)

    graph_filename = sys.argv[1]
    graph_index = sys.argv[2]

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
    bfs(grafo, graph_index)


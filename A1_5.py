"""
Algoritmo Floyd-Warshall

Crie um programa que recebe um arquivo de grafo como argumento. O
programa devera exercutar o algoritmo de Floyd-Warshall e mostrar as distancias para cada par de vertices na tela
utilizando o formato do exemplo abaixo. Na saida, cada linha tera as distancias para vertice na ordem crescente
dos indices informados no arquivo de entrada
"""
import os, sys
from grafo import Grafo
from math import inf

def floyd_warshall(graph: Grafo):
    # Inicializa a matriz de distancias com inf
    n = graph.qtdVertices()
    distancias = [[inf] * n for _ in range(n)]
    
    # Preencher a matriz de distâncias com as distâncias conhecidas
    for u in range(n):
        distancias[u][u] = 0
        for v in range(n):
            if (u+1, v+1) in graph.w:
                distancias[u][v] = graph.w[(u+1, v+1)]
                distancias[v][u] = graph.w[(u+1, v+1)]
    
     # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

def imprimir_saida(distancias):
    for i, linha in enumerate(distancias):
        print(f"{i + 1}:{','.join(str(d) if d != inf else 'inf' for d in linha)}")

if __name__ == "__main__":
    if len(sys.argv) < 1 or len(sys.argv) > 3:
        print('\n> Uso: python A1_5.py graph_filename\n')
        sys.exit(1)

    graph_filename = sys.argv[1]

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

    # Executa o Floyd-Warshall
    distancias = floyd_warshall(grafo)

    imprimir_saida(distancias)

"""
Algoritmo de Dijkstra

Uso: python A1_4.py graph_filename graph_index

Crie um programa que recebe um arquivo de grafo como
argumento e um vertice s. O programa devera executar o algoritmo de Bellman-Ford ou de Dijkstra e informar o
caminho percorrido de s ate todos os outros vertices do grafo e a distancia necessaria. A saida devera ser impressa
na tela de acordo com o exemplo abaixo. Cada linha representa o caminho realizado de s para o vertice da respectiva
linha. Em cada linha, antes dos simbolo “:” devera estar o vertice destino. A direita de “:”, encontra-se o caminho `
percorrido de s ate o vertice destino. Mais `a direita encontram-se os simbolos “d=” seguidos da distancia necessaria
para percorrer o caminho.

"""
import os, sys
from A1_1 import Grafo
from math import inf

def dijkstra(graph: Grafo, origin_index):
    # Inicialização das estruturas
    origin_vertex = graph.V[origin_index-1]  # Obtém o vértice de origem pelo índice
    D = {v: inf for v in graph.V}
    A = {v: None for v in graph.V}
    C = {v: False for v in graph.V}
    caminho_minimo = {v: [] for v in graph.V}  # Armazena o caminho mínimo para cada vértice destino

    D[origin_vertex] = 0

    while any(not C[v] for v in graph.V):
        u = min((v for v in graph.V if not C[v]), key=lambda x: D[x]) # Retornar o vértice de custo mínimo
        C[u] = True

        # OBS: vizinhos(v: int) -> recebe um inteiro e não um vertice
        for vizinho in graph.adjacencias(u):
            if not C[vizinho]:  # Verifica se o vizinho não foi visitado
                if (u[0], vizinho[0]) in graph.w:
                    peso = graph.w[(u[0], vizinho[0])]  # Obtém o peso da aresta (u, vizinho) do dicionário w
                elif (vizinho[0], u[0]) in graph.w:
                    peso = graph.w[(vizinho[0], u[0])]  # Obtém o peso da aresta (vizinho, u) do dicionário w

                # Atualiza a distância se o caminho através de u for menor
                if D[vizinho] > D[u] + peso:
                    D[vizinho] = D[u] + peso
                    A[vizinho] = u
                    caminho_minimo[vizinho] = caminho_minimo[u] + [vizinho]  # Atualiza o caminho mínimo para o vértice destino

    # Monta a saída desejada
    resultado = ""
    for destino, caminho in caminho_minimo.items():
        if caminho:
            caminho_str = ",".join(str(v[0]) for v in [origin_vertex] + caminho)
            resultado += f"{destino[0]}: {caminho_str}; d={D[destino]}\n"
        else:
            resultado += f"{destino[0]}: {destino[0]}; d={D[destino]}\n"

    return resultado


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('\n> Uso: python A1_4.py graph_filename graph_index\n')
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

    # Executa o algoritmo de Dijkstra e imprime na tela o resultado
    resultado =  dijkstra(grafo, graph_index)
    print(resultado)
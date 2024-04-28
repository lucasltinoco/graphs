""" CICLO EULERIANO - Algoritmo de Hierholzer """
import sys, os
from grafo import Grafo
from random import choice

def buscarSubCicloEuleriano(graph, v, C):
    return
    ciclo = [v]  # Inicializa o ciclo com o vértice v
    t = v

    while True:
        # Procura por uma aresta não visitada conectada ao último vértice do ciclo
        arestas_nao_visitadas = [aresta for aresta in graph.vizinhos(v) if not C[aresta]]
        
        if not arestas_nao_visitadas:
            return (False, None)  # Não há arestas não visitadas, retorna falso

        u, _ = arestas_nao_visitadas[0]  # Seleciona a primeira aresta não visitada
        C[(v, u)] = True  # Marca a aresta como visitada
        ciclo.append(u)  # Adiciona o vértice u ao ciclo
        v = u

        if v == t:
            break  # Termina o loop quando alcança o vértice inicial do ciclo

    # Verifica se há vértices no ciclo com arestas adjacentes não visitadas
    for x in ciclo:
        for u, w in graph.adjacencias(x):
            if not C[(u, w)]:
                r, ciclo0 = buscarSubCicloEuleriano(graph, x, C)
                if not r:
                    return (False, None)
                
                # Insere ciclo0 na posição de x em ciclo
                index_x = ciclo.index(x)
                ciclo = ciclo[:index_x] + ciclo0 + ciclo[index_x + 1:]

    return True, ciclo  # Retorna verdadeiro e o ciclo euleriano encontrado


def ciclo_euleriano(graph: Grafo):
    C = []
    for aresta in graph.E:
        C.append(False)

    v = None
    lista_vertices = [vertice for vertice in graph.V if graph.grau(vertice[0]) > 0]

    if lista_vertices:
        v = choice(lista_vertices)
        print(v)
    else:
        print("Não há vértices com grau maior que 0 no grafo.")

    r, ciclo = buscarSubCicloEuleriano(graph, v, C)

    if not r:
        return (False, None)
    else:
        if False in C:
            return (False, None)
        else:
            return (True, ciclo)

def eulerian_cycle(graph: Grafo):
    C = {}
    v = 0

    # Cria o vetor C com valor False para todos elementos
    for i in range(graph.qtdArestas()):
        C[graph.E[i]] = False

    # Seleciona arbitrariamente um vertice
    for i in range(1, graph.qtdVertices() + 1):
        if graph.grau(i) > 0:
            v = i
            break

    if v == 0:
        print("\n> Não existe ciclo euleriano\n")
        return

#     (r, cycle) = find_eulerian_subcycle(graph, v, C)
#     print(r, cycle)
    





if __name__ == "__main__":
    if len(sys.argv) < 1 or len(sys.argv) > 3:
        print('\n> Uso: python bfs.py graph_filename\n')
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

    # Executa o ciclo_euleriano
    ciclo_euleriano(grafo)
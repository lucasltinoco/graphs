"""
EULERIAN CYCLE IDENTIFIER

Algoritmo criado para identificar um ciclo euleriano em um grafo.

Uso: python A1_3.py graph_filename

args: 
    graph: Grafo()
"""

from grafo import Grafo
import sys, os
import random


def hierholzer(graph: Grafo):
    C = {}
    vertices = graph.V
    edges = graph.E

    for x in edges:
        C[x] = False

    v = random.choice(vertices)
    r, ciclo = find_eulerian_subcycle(graph, v[0], C)

    if r == False:
        return False, None

    else:
        if False in C.values():
            return False, None
        else:
            return True, ciclo


def find_eulerian_subcycle(graph, v, C):
    ciclo = [v]
    t = v

    while True:
        if not False in C.values():
            return False, None
        else:
            not_visited = []

            for k, i in C.items():
                if i == False and (k[0] == v or k[1] == v):
                    not_visited.append(k)

            used = v
            v = not_visited[0][0]
            u = not_visited[0][1]
            C[(v, u)] = True
            v = u if u != used else v
            ciclo.append(v)

        if v == t:
            break

    vertices_in_cycle = [x for x in graph.V if x[0] in ciclo]
    open_neighbors = []

    for x in vertices_in_cycle:
        for y in graph.adjacencias(x):
            if (x, y) in C:
                if C[(x, y)] == False:
                    open_neighbors.append(x)

            elif (y, x) in C:
                if C[(y, x)] == False:
                    open_neighbors.append(x)

    if not open_neighbors:
        return True, ciclo

    for x in open_neighbors:
        r, ciclo_2 = find_eulerian_subcycle(graph, x, C)

        if r == False:
            return False, None

        for x in ciclo:
            if x == ciclo_2[0]:
                index = ciclo.index(x)
                ciclo[index + 1 : index + 1] = ciclo_2
                ciclo.pop(index)
                break

        return True, ciclo


def print_output(result: tuple):
    (has_eulerian, cycle) = result

    if has_eulerian:
        cycle_str = ",".join(str(v) for v in cycle)
        print(1)
        print(cycle_str)
    else:
        print(0)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("\n> Uso: python eulerian.py graph_filename graph_index\n")
        sys.exit(1)

    graph_filename = sys.argv[1]

    # Verifica se o nome do arquivo passado existe
    if not os.path.exists(graph_filename):
        print(f"\n> graph_filename: {graph_filename} não existe\n")
        sys.exit(1)

    try:
        grafo = Grafo()  # Inicializa o grafo vazio
        grafo.ler(graph_filename)  # Adiciona elementos ao grafo
    except Exception as e:
        print(f"\n> Erro ao incializar o grafo: {e}\n")
        sys.exit(1)

    # Executa a busca em largura
    result = hierholzer(grafo)
    print_output(result)

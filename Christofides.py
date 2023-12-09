## -----------------------------------------------------------------------------------------------------
##  Arquivo     : Christofides.py
##  Conteúdo    : Implementação da função que calcula a solução aproximativa do caixeiro viajante pelo método de Christofides
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------
import networkx as nx
import time
import psutil

## @brief Encontra o uso de memória em bytes    
def getMemoryUsage():
    process = psutil.Process()
    return process.memory_info().rss

## @brief Encontra o circuito hamiltoniano usando o algoritmo de Christofides
def christofides(graph, n):
    # Registra o tempo de início e o uso de memória antes da execução
    startTime = time.time()  
    startMemory = getMemoryUsage()

    # 1. Computa T uma árvore geradora mínima do grafo.
    T = nx.minimum_spanning_tree(graph)

    # 2. Seja I o conjunto de vértices de grau ímpar de T. 
    oddDegreeNodes = [i for i in T.nodes if T.degree(i) % 2 ]
    
    # 3. Compute M um matching perfeito de peso mínimo no subgrafo induzido por I. 
    M = nx.min_weight_matching(nx.subgraph(graph, oddDegreeNodes))

    # 4. Seja G o multigrafo formado com os vértices do grafo e arestas de M e T.
    G = nx.MultiGraph()
    G.add_nodes_from(range(1, n))
    G.add_edges_from(T.edges())
    G.add_edges_from(M)

    # 5. Computa o circuito euleriano em G 
    initialTour = list(nx.eulerian_circuit(G, source = 1))

    # 6. Elimina vértices duplicados, substituindo subcaminhos u-w-v por arestas u-v
    tour = [ 1 ]
    for (i,j) in initialTour:
        if j not in tour:
            tour.append(j)

    # Calcula o tempo total de execução do algoritmo
    endTime = time.time()
    finalTime = endTime - startTime  

    # Calcula a memória utilizada pelo algoritmo
    endMemory = getMemoryUsage()
    finalMemory = endMemory - startMemory

    return tour, finalTime, finalMemory

def getPathWeight(graph, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += graph[path[i]][path[i+1]]['weight']
    return weight

def solveTSP(graph):
    n = graph.number_of_nodes()
    tour, time, memory = christofides(graph, n)
    answer = getPathWeight(graph, tour)
    print("-----------------------")
    print("Tempo de execução: ", time)
    print("Custo de memória: ", memory)
    return answer 
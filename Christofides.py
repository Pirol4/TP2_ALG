## -----------------------------------------------------------------------------------------------------
##  Arquivo     : Christofides.py
##  Conteúdo    : Implementação da função que calcula a solução aproximativa do caixeiro viajante pelo método de Christofides
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------

import networkx as nx
import time
import psutil

TIME_OUT = 1800 # Tempo máximo permitido para execução dos algoritmos (30 minutos)

## @brief Identifica os vértices de grau ímpar em um grafo
def getOddVertices(graph):  
    oddVertices = [vertex for vertex, degree in graph.degree() if degree % 2 != 0]
    return oddVertices

## @brief Encontra a Árvore de Espalhamento Mínima em um grafo
def getMinimumSpanningTree(graph):  
    return nx.minimum_spanning_tree(graph)

## @brief Encontra o emparelhamento de peso mínimo em um subgrafo
def getMinimumWeightMatching(graph, vertex):  
    subgraph = graph.subgraph(vertex)
    return nx.max_weight_matching(subgraph)

## @brief Encontra um circuito euleriano em um grafo
def getEulerianCircuit(graph, startVertex):
    return list(nx.eulerian_circuit(graph, source=startVertex))

## @brief Encontra o uso de memória em bytes    
def getMemoryUsage():
    process = psutil.Process()
    return process.memory_info().rss

## @brief Resolve o Problema do Caixeiro Viajante usando o algoritmo de Christofides
def Christofides(graph):
    # Registra o tempo de início e o uso de memória antes da execução
    startTime = time.time()  
    startMemory = getMemoryUsage()

    # 1. Computamos T, uma árvore geradora mínima do grafo
    T = getMinimumSpanningTree(graph)

    # 2. Seja I o conjunto de vértices de grau ímpar de T
    I = getOddVertices(T)

    # 3. Computamos M, um matching perfeito de peso mínimo do subgrafo induzido por I
    M = getMinimumWeightMatching(graph, I)

    # 4. Seja G o multigrafo formado com os vértices de V e aresta de M e T.
    G = T.copy()
    G.add_edges_from(M)

    # 5. Encontramos um circuito euleriano em G
    eulerianCircuitEdges = getEulerianCircuit(G, startVertex=0)

    # 6. Eliminamos vértices duplicados, substituindo caminhos u-w-v por u-v
    eulerianPath = list(dict.fromkeys([edge[0] for edge in eulerianCircuitEdges]))

    # 7. Gerar o circuito hamiltoniano
    answer = [eulerianPath[0]]
    for vertex in eulerianPath[1:]:
        if vertex not in answer:
            answer.append(vertex)

    # Calcula o tempo total de execução do algoritmo
    endTime = time.time()
    finalTime = endTime - startTime  

    # Cálcula a memória utilizada pelo algoritmo
    endMemory = getMemoryUsage()
    finalMemory = endMemory - startMemory

    # Verifica se a execução passou dos tempo estipulado
    if finalTime > TIME_OUT:
        return {'path': None, 'time': 'NA', 'memory': 'NA', 'quality': 'NA'}

    return {'path': answer, 'time': finalTime, 'memory': finalMemory}

# Exemplo de uso
if __name__ == "__main__":
    graph = nx.complete_graph(51)
    for edge in graph.edges():
        graph.edges[edge]['weight'] = 1

    tsp_solution = Christofides(graph)

    print("Solução do Caixeiro Viajante:", tsp_solution['path'])
    print("Tempo de Execução:", tsp_solution['time'])
    print("Uso de Memória:", tsp_solution['memory_used'], "bytes")
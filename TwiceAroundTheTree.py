## -----------------------------------------------------------------------------------------------------
##  Arquivo     : TwiceAroundTheTree.py
##  Conteúdo    : Implementação da função que calcula a solução aproximativa do caixeiro viajante pelo método TwiceAroundTheTree
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------
import networkx as nx
import time
import psutil
    
## @brief Encontra o uso de memória em bytes    
def getMemoryUsage():
    process = psutil.Process()
    return process.memory_info().rss

## @brief Encontra o circuito hamiltoniano usando o algoritmo Twice Around The Tree
def twiceAroundTheTree(graph):
    # Registra o tempo de início e o uso de memória antes da execução
    startTime = time.time()
    startMemory = getMemoryUsage()

    # 1. Computa T uma árvore geradora mínima do grafo.
    T = nx.minimum_spanning_tree(graph)

    # 2. Seja H uma lista dos vértices, ordenados pela visitação em pré-ordem de T
    tour = list(nx.dfs_preorder_nodes(T, 1))
    
    # 3. Ele precisa voltar para a posição inicial
    tour.append(tour[0])

    # Calcula o tempo total de execução do algoritmo
    endTime = time.time()
    finalTime = endTime - startTime  

    # Cálcula a memória utilizada pelo algoritmo
    endMemory = getMemoryUsage()
    finalMemory = endMemory - startMemory

    return tour, finalTime, finalMemory

## @brief Calculate the path weight
def getPathWeight(graph, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += graph[path[i]][path[i+1]]['weight']
    return weight

## @brief General function to find the answer
def solveTSP(graph):
    tour, time, memory = twiceAroundTheTree(graph)
    answer = getPathWeight(graph, tour)
    print("-----------------------")
    print("Twice Around the Tree")
    print("Tempo de execução: ", time)
    print("Custo de memória: ", memory)
    return answer 

## -----------------------------------------------------------------------------------------------------
##  Arquivo     : TwiceAroundTheTree.py
##  Conteúdo    : Implementação da função que calcula a solução aproximativa do caixeiro viajante pelo método TwiceAroundTheTree
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------

import networkx as nx
import time
import psutil

TIME_OUT = 1800 # Tempo máximo permitido para execução dos algoritmos (30 minutos)
    
## @brief Encontra a Árvore de Espalhamento Mínima em um grafo
def getMinimumSpanningTree(graph):  
    return nx.minimum_spanning_tree(graph)

## @brief Encontra o uso de memória em bytes    
def getMemoryUsage():
    process = psutil.Process()
    return process.memory_info().rss

def TwiceAroundTheTree(graph):
    # Registra o tempo de início e o uso de memória antes da execução
    startTime = time.time()
    startMemory = getMemoryUsage()

    # 1. Encontrar a Árvore de Espalhamento Mínima (MST)
    MST = getMinimumSpanningTree(graph)

    # 2. Seja H uma lista de vertices, ordenados em ordem de pré ordem da Árvore de Espalhamento Mínima encontramos o circuito hemiltoniano de H 
    answer = list(nx.dfs_preorder_nodes(MST, source=0))
    answer.append(answer[0])  # Fechar o circuito

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
    # Resolver o Problema do Caixeiro Viajante usando o Twice Around the Tree
    tsp_solution = twice_around_the_tree_tsp(graph)

    print("Solução do Caixeiro Viajante (Twice Around the Tree):", tsp_solution['path'])
    print("Tempo de Execução:", tsp_solution['time'])
    print("Espaço de Execução:", tsp_solution['memory'])

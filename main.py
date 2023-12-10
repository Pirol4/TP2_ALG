## -----------------------------------------------------------------------------------------------------
##  Arquivo     : main.py
##  Conteúdo    : Implementação da função que chama todos os métodos
##  Aluno       : Filipe Pirola Santos
## -----------------------------------------------------------------------------------------------------
import Christofides as C
import TwiceAroundTheTree as T
import BranchAndBound as B
import tsplib95 as tsp
import sys
    
## @brief Carrega instância do TSPLIB
def getGraph(file_path):

    problem = tsp.load(file_path)

    graph = problem.get_graph()

    return graph

def main():
    
    problem = sys.argv[1]
    graph = getGraph(problem)
    
    print("RESULTADO: ", T.solveTSP(graph))
    print("RESULTADO: ", C.solveTSP(graph))
    print("RESULTADO: ", B.solveTSP(graph))

main()
    
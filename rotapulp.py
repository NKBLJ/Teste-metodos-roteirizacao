import pulp
import numpy as np

def rota_prog_linear(distancias):
    # Exemplo de matriz de distâncias (substitua isso com a sua matriz)
    distancias = np.array(distancias)
    np.fill_diagonal(distancias, np.max(distancias)*10)
    
    num_cities = len(distancias)
    
    # Criação do problema de minimização
    prob = pulp.LpProblem("TSP", pulp.LpMinimize)
    
    # Variáveis de decisão
    x = [[pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary) for j in range(num_cities)] for i in range(num_cities)]
    
    # Função objetivo (minimizar a distância total)
    prob += pulp.lpSum(distancias[i][j] * x[i][j] for i in range(num_cities) for j in range(num_cities)), "FuncaoObjetivo"
    
    # Restrição: cada cidade é visitada exatamente uma vez
    for i in range(num_cities):
        prob += pulp.lpSum(x[i][j] for j in range(num_cities)) == 1, f"VisitaUmaVez_{i}"
    
    # Restrição: sai de cada cidade exatamente uma vez
    for j in range(num_cities):
        prob += pulp.lpSum(x[i][j] for i in range(num_cities)) == 1, f"SaiUmaVez_{j}"
    
    
    # Restrições para evitar sub-rotas (arcos fechados)
    u = [pulp.LpVariable(f"u_{i}", cat=pulp.LpInteger, lowBound=0, upBound=num_cities - 1) for i in range(num_cities)]
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                prob += u[i] - u[j] + num_cities * x[i][j] <= num_cities - 1, f"SubRota_{i}_{j}"
    
    
    # Resolver o problema
    prob.solve()
    
    # Resultados
    dist_total = 0
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i][j]) == 1:
                dist_total += distancias[i][j]
    return round(dist_total)

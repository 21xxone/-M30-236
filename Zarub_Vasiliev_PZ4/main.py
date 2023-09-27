import pulp
import time
from pulp import value, lpSum

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += -x1 + 7*x2 - 2*x3 - 2*x4 + x5 == 5
problem += 2*x1 + 2*x2 - x3 + x5 == 18
problem += 2*x1 - 4*x2 + x3 + x4 == 8
problem += lpSum([11*x1, -4*x2, 2*x3,-5*x4, 2*x5])
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
stop = time.time()
print ("Время :")
print(stop - start)
#10 задание стр.60
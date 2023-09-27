import pulp
import time
from pulp import value, lpSum

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMinimize)
problem += -2*x1 + x2 + x3 + x4 == 4
problem += -1*x1 + x2 + 3*x3 + x5 == 6
problem += x1 - 3*x2 + x3*3 + x6 == 2
problem += lpSum([-2*x1, -4*x2, -2*x3, x4, x5, x6])
problem.solve()
print ("Результат2:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
stop = time.time()
print ("Время :")
print(stop - start)
#22 задание стр.62
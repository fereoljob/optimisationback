from django.http import HttpResponse
from minizinc import Instance, Model, Solver
import os
from .utils import checkCompleteSolution,checkPartialSolution,parseSolutionForFront
import json


baseVariables = ["enum TRANSPORT ={Train, Boat, Plane}","enum PAYS = {Belgique, Italie, Angleterre}","array[PERSON] of var TRANSPORT : voyage_par","array[PERSON] of var PAYS : va_en"]
baseConstraints = ["constraint all_different(voyage_par)","constraint all_different(va_en)"]
userVariables = []
userConstraints = []

def testPartialSolution(request,problem_id,partialsol):
    model_path = os.path.join('static','modelresolver','model'+str(problem_id)+'.mzn')
    model = Model(model_path)
    solver = Solver.lookup("gecode")
    instance = Instance(solver,model)
    result = instance.solve(all_solutions=True)
    return HttpResponse(checkPartialSolution(result,partialsol))

def resolveProbleme(request,problem_id,user_solution):
    model_path = os.path.join('static','modelresolver','model'+str(problem_id)+'.mzn')
    model = Model(model_path)
    solver = Solver.lookup("gecode")
    instance = Instance(solver,model)
    result = instance.solve(all_solutions=True)
    return HttpResponse(checkCompleteSolution(result,user_solution))

def addVariable(request,variable):
    variable = variable.split("|")
    global userVariables 
    userVariables = []
    tmp = []
    for v in range(0,len(variable)):
        tmp.append(variable[v])
    userVariables = tmp
    return HttpResponse(True)

def addConstraint(request,constraints):
    constraints = constraints.split("|")
    global userconstraints
    userconstraints = []
    tmp = []
    for c in range(0,len(constraints)):
        tmp.append(constraints[c])
    userConstraints = tmp
    userModel = os.path.join('static','modelresolver','userModel.mzn')
    if os.path.exists(userModel):
        os.remove(userModel)
    f = open(userModel,'at')
    f.write("include \"globals.mzn\"; \n")
    for value in userVariables:
        value+="; \n"
        f.write(value)
    for value in baseVariables:
        value+="; \n"
        f.write(value)
    for value in baseConstraints:
        value+="; \n"
        f.write(value)
    for value in userConstraints:
        value+="; \n"
        f.write(value)
    f.write("solve satisfy; \n")
    sortie = """
output
["{Name:"++show(p)
++",Transport:"++show(voyage_par[p])
++",Pays:"++show(va_en[p])++"}"
++ "|"
| p in PERSON];
    """
    f.write(sortie)
    f.close()
    model = Model(userModel)
    solver = Solver.lookup("gecode")
    instance = Instance(solver,model)
    result  = instance.solve(all_solutions=True)
    if result.status.has_solution():
        sol = parseSolutionForFront(result)
    else:
        sol = "No solutions"
    response  = {
        "hasSolution" : result.status.has_solution(),
        "solutions" : sol
        }
    response = json.dumps(response,indent=4)
    print(response)
    return HttpResponse(response)




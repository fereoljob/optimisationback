from django.http import HttpResponse
from minizinc import Instance, Model, Solver
import os
from .utils import checkCompleteSolution,checkPartialSolution, MyModel,parseSolutionForFront
import json



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
    MyModel.userVariables = []
    for v in range(0,len(variable)):
        MyModel.userVariables.append(variable[v])
    return HttpResponse(True)

def addConstraint(request,constraints):
    constraints = constraints.split("|")
    MyModel.constraints = []
    for c in range(0,len(constraints)):
        MyModel.userConstraints.append(constraints[c])
    userModel = os.path.join('static','modelresolver','userModel.mzn')
    if os.path.exists(userModel):
        os.remove(userModel)
    f = open(userModel,'at')
    f.write("include \"globals.mzn\";")
    for value in MyModel.baseVariables:
        value+="; \n"
        f.write(value)
    for value in MyModel.userVariables:
        value+="; \n"
        f.write(value)
    for value in MyModel.baseConstraints:
        value+="; \n"
        f.write(value)
    for value in MyModel.userVariables:
        value+="; \n"
        f.write(value)
    f.write("solve satisfy")
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
    print(json.dump(response))
    return HttpResponse(json.dump(response))




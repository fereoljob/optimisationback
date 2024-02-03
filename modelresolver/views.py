from django.http import HttpResponse
from minizinc import Instance, Model, Solver
import os
from .utils import checkCompleteSolution,checkPartialSolution

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


from django.http import HttpResponse
from minizinc import Instance, Model, Solver
import os
from .utils import checkUserSolution, compareSol, checkIfContains, checkUserPartial

def testPartialSolution(request,problem_id,partialsol):
    model_path = os.path.join('static','modelresolver','model'+str(problem_id)+'.mzn')
    model = Model(model_path)
    solver = Solver.lookup("gecode")
    instance = Instance(solver,model)
    result = instance.solve(all_solutions=True)
    return HttpResponse(checkUserPartial(result,partialsol))

def resolveProbleme(request,problem_id,user_solution):
    model_path = os.path.join('static','modelresolver','model'+str(problem_id)+'.mzn')
    model = Model(model_path)
    solver = Solver.lookup("gecode")
    instance = Instance(solver,model)
    result = instance.solve(all_solutions=True)
    return HttpResponse(checkUserSolution(result,user_solution))


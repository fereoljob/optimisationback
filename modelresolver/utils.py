import json

def checkCompleteSolution(solution,completeSolution):
    soluChaine = completeSolution.strip("|")
    tab = soluChaine.split("|")
    for sol in range(0,solution.__len__()):
        solverSol = str(solution[sol]).strip("|")
        solverSolTab = solverSol.split("|")
        if len(solverSolTab)!=len(tab):
            return False
        if compareSolComplete(solution[sol],tab,len(tab)):
            return True
    return False

def checkPartialSolution(solution,partialSolution):
    tab = partialSolution.split("|")
    for sol in range(0,solution.__len__()):
        if compareSolPartial(solution[sol],tab,len(tab)):
            return True
    return False

def compareSolComplete(sol1,soluser,size):
    if size==0:
        return True
    if checkIfContainsComplete(sol1,soluser[size-1]):
        return compareSolComplete(sol1,soluser,size-1)
    else:
        return False
    
def checkIfContainsComplete(sol1,ligne):
    solverSol = str(sol1).strip("|")
    solverSolTab = solverSol.split("|")
    for i in range(0,len(solverSolTab)):
        dict1 = json.loads(solverSolTab[i])
        dict2 = json.loads(ligne)
        if len(dict1)!=len(dict2):
            return False
        else:
            if dict1==dict2:
                return True
    return False

def compareSolPartial(sol1,soluser,size):
    if size==0:
        return True
    if checkIfContainsPartial(sol1,soluser[size-1]):
        return compareSolPartial(sol1,soluser,size-1)
    else:
        return False

def checkIfContainsPartial(sol1,ligne):
    solverSol = str(sol1).strip("|")
    solverSolTab = solverSol.split("|")
    for i in range(0,len(solverSolTab)):
        dict1 = json.loads(solverSolTab[i])
        dict2 = json.loads(ligne)
        if customComparePartial(dict1,dict2,0):
            return True
    return False

def customComparePartial(obj1,obj2,depth):
    if depth==len(obj2):
        return True
    if obj1.get(depth)==obj2.get(depth):
        return customComparePartial(obj1,obj2,depth+1)
    else:
        return False

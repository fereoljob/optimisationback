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
    partialSolution = partialSolution.strip("|")
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
        if customComparePartial(dict1,dict2):
            return True
    return False


def customComparePartial(obj1,obj2):
    for propertyName in obj2:
        if obj1.get(propertyName)!=obj2.get(propertyName):
            return False
    return True

class MyModel:
    baseVariables = ["enum TRANSPORT ={Train, Boat, Plane}","enum PAYS = {Belgique, Italie, Angleterre}","array[PERSON] of var TRANSPORT : voyage_par","array[PERSON] of var PAYS : va_en"]
    baseConstraints = ["constraint all_different(voyage_par)","constraint all_different(va_en)"]
    userVariables = []
    userConstraints = []
def parseSolutionForFront(resultat):
    chaine = "Solution(s) ["
    for res in range(0,len(resultat)):
        chaine+= "{",str(resultat[res]),"}"
    chaine+="]"
    return chaine



    


def checkUserSolution(solution,usersolution):
    tab = usersolution.split("|")
    for sol in range(0,solution.__len__()):
        tab2 = str(solution[sol]).split("|")
        if tab2==tab:
            return True
    return False

def checkUserPartial(solution,partialSolution):
    tab = partialSolution.split("|")
    for sol in range(0,solution.__len__()):
        if compareSol(solution[sol],tab,len(tab)):
            return True
    return False

def compareSol(sol1,soluser,size):

    if(size==0):
        return True
    if checkIfContains(sol1,soluser[size-1]):
        return compareSol(sol1,soluser,size-1)
    else:
        return False
    
def checkIfContains(sol1,ligne):
    tab = str(sol1).split("|")
    print(tab)
    for i in range(0,len(tab)-1):
        if tab[i]==ligne:
            return True
    return False

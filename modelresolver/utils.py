def checkProblem(solution,usersolution):
    for sol in range(0,solution.__len__()-1):
        print(len(usersolution))
        tab = usersolution.split("|")
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
    print(len(tab))
    for i in range(0,len(tab)-1):
        print(tab[i])
        print("compare to:")
        print(ligne)
        if tab[i]==ligne:
            return True
    return False

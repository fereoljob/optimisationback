def checkProblem(solution,usersolution):
    tab = usersolution.split("|")
    for sol in range(0,solution.__len__()):
        tab2 = str(solution[sol]).split("|")
        if tab2==tab:
            return True
    return False
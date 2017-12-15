def bottomProgram(programs):
    for i in range(len(programs)):
        if len(programs[i]) != 2:
            test = programs[i][0]
            found = 0
            for entry in programs:
                if len(entry) != 2:
                    for i in range(3, len(entry)):
                        if entry[i] == test:
                            found = 1
            if found == 0:
                return test

def programList(f):
    inFile = open(f,'r')
    programs = [ element.split() for element in inFile.read().split('\n') ]

    for entry in programs:
        if len(entry) != 2:
            for i in range(3,len(entry)-1):
                entry[i] = entry[i][:-1]
    inFile.close()
    return programs

def programDict(pList):
    pDict = {}
    for entry in pList:
        if len(entry) == 2:
            pDict[entry[0]] =[entry[1][1:-1]]
        else:
            pDict[entry[0]] =[entry[1][1:-1]]+entry[3:]
    return pDict

def towerWeights(programs):
    weights = []
    pDict = programDict(programs)
    for item in programs:
        if len(item) != 2:
            weights.append( (sumTower(item[0], pDict), item[0]) )
    weights.sort(reverse=True)
    return weights

def towerWeight(p, programs):
    pDict = programDict(programs)
    oldweights = []
    diff = 0
    for j in range(5):
        weights = [p]
        if len(pDict[p]) > 1:
            pList = pDict[p]
            for i in range(1,len(pList)):
                weights.append( (sumTower(pList[i], pDict), pList[i]) )
        wdiffIndex = 1
        for i in range(2,len(weights)):
            done = True
            if weights[wdiffIndex][0] != weights[i][0]:
                diff = weights[wdiffIndex][0] - weights[i][0]
                wdiffIndex = i
                done = False
                break
        if done:
            return int(pDict[p][0]) + diff
        p = weights[wdiffIndex][1]
        #print(weights)
        oldweights = weights
    return 0

def sumTower(p,d):
    if len(d[p]) == 1:
        return int(d[p][0])
    else:
        total = int(d[p][0])
        for entry in d[p][1:]:
            total = total + sumTower(entry,d)
        return total

#print(bottomProgram(programList("programTower1.txt")))
#print(bottomProgram(programList("programTower2.txt")))
#print(programList("programTower1.txt"))
#print(programDict(programList("programTower1.txt")))
print(towerWeight(bottomProgram(programList("programTower2.txt")),programList("programTower2.txt")))
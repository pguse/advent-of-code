inFile = open("programsDay12.txt",'r')
programs = inFile.read().split('\n')
inFile.close()

pDict = {}
for i in range(len(programs)):
    pList = programs[i].split()
    pDict[pList[0]] = pList[2:]

# Strip Commas
for k in pDict.keys():
    for i in range(len(pDict[k])):
        if pDict[k][i][-1] == ",":
            pDict[k][i] = pDict[k][i][:-1]

test = {'0':['2'], '1':['1'], '2':['0','3','4'], '3':['2','4'], '4':['2','3','6'], '5':['6'], '6':['4','5']}

def count(d):
    programs = ['0']
    depth = 0
    for k in d.keys():
        if len(d[k]) > depth:
            depth = len(d[k])
    for i in range(depth*2):
        for k in d.keys():
            for item in d[k]:
                    if item in programs and (k not in programs):
                        programs.append(k)
                        break
        #print(programs)

    return len(programs)

def numGroups(d):
    depth = 0
    for k in d.keys():
        if len(d[k]) > depth:
            depth = len(d[k])
    programs = []
    n = 0
    for k in d.keys():
        group = []
        if k not in programs:
            n += 1
            group.append(k)
            overlap = False
            for i in range(depth*2):
                for k in d.keys():
                    for item in d[k]:
                            if item in group and (k not in group):
                                group.append(k)
                                break
            for item in group:
                if item in programs:
                    overlap = True
                else:
                    programs.append(item)
            if overlap:
                n -= 1
        #print(programs)
    return n

print(count(test))
print(count(pDict))
print(numGroups(test))
print(numGroups(pDict))
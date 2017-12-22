import copy

# Parse the input file into a Dictionary
inFile = open("layers.txt",'r')
layers = [ item.split() for item in inFile.read().split('\n') ]

layersDict = {}
for item in layers:
    layersDict[item[0][:-1]] = int(item[1])
#print(layersDict)

def getSeverity(layersDict):
    # Test
    #layersDict = {'0':3, '1':2, '4':4, '6':4}
    # Find the max number of layers
    num_layers = -1
    for k in layersDict.keys():
        if int(k) > num_layers:
            num_layers = int(k)
    num_layers += 1

    # Build the firewall
    firewall = []
    direction = []
    for i in range(num_layers):
        firewall.append([])
        direction.append(-1)
        if str(i) in layersDict.keys():
            for j in range(layersDict[str(i)]):
                firewall[i].append(0)

    # Intialize the Scanners
    for layer in firewall:
        if len(layer) != 0:
            layer[0] = 1

    #print(firewall)
    # Scan the firewall
    severity = 0
    for k in range(1, num_layers):
        for i in range(num_layers):
            for j in range(len(firewall[i])):
                if firewall[i][j] == 1:
                    if j == len(firewall[i])-1 or j == 0:
                        direction[i] *= -1
                    firewall[i][j] = 0
                    firewall[i][j + direction[i]] = 1
                    break
        if len(firewall[k]) > 0:
            if firewall[k][0] == 1:
                severity = severity + (k*len(firewall[k]))
        #print(firewall, severity)
        #print(direction)
        #input()

    return severity


    # Scan the firewall
    firewall = list(f)
    for k in range(delay):
        for i in range(len(firewall)):
            for j in range(len(firewall[i])):
                if firewall[i][j] == 1:
                    if j == len(firewall[i])-1 or j == 0:
                        direction[i] *= -1
                    firewall[i][j] = 0
                    firewall[i][j + direction[i]] = 1
                    break
    return firewall

def getDelay_old(layersDict):
    # Test
    #layersDict = {'0':3, '1':2, '4':4, '6':4}
    # Find the max number of layers
    num_layers = -1
    for k in layersDict.keys():
        if int(k) > num_layers:
            num_layers = int(k)
    num_layers += 1

    # Build the firewall
    firewall = []
    direction = []
    for i in range(num_layers):
        firewall.append([])
        direction.append(-1)
        if str(i) in layersDict.keys():
            for j in range(layersDict[str(i)]):
                firewall[i].append(0)

    # Intialize the Scanners
    for layer in firewall:
        if len(layer) != 0:
            layer[0] = 1
    
    original_firewall = copy.deepcopy(firewall)
    original_direction = list(direction)
    # Scan the firewall
    delay = 1
    while True:
        caught = False
        # Delay the firewall
        for k in range(delay):
            for i in range(num_layers):
                for j in range(len(firewall[i])):
                    if firewall[i][j] == 1:
                        if j == len(firewall[i])-1 or j == 0:
                            direction[i] *= -1
                        firewall[i][j] = 0
                        firewall[i][j + direction[i]] = 1
                        break
        #print(firewall)

        for k in range(num_layers):
            if len(firewall[k]) > 0:
                if firewall[k][0] == 1:
                    if k == 86:
                        print(delay)
                    caught = True
            for i in range(num_layers):
                for j in range(len(firewall[i])):
                    if firewall[i][j] == 1:
                        if j == len(firewall[i])-1 or j == 0:
                            direction[i] *= -1
                        firewall[i][j] = 0
                        firewall[i][j + direction[i]] = 1
                        break
        if caught:
            firewall = copy.deepcopy(original_firewall)
            direction = list(original_direction)
            delay += 1
        else:
            break
    return delay

def getDelay(layersDict):
    #layersDict = {'0':3, '1':2, '4':4, '6':4}
    delay = 0
    N = 100000000
    caughtDelays = [0]*N
    caughtDelays[0] = 1
    for k in layersDict.keys():
        factor = (layersDict[k] - 1) * 2 - int(k)
        if factor == 0 and str(k) != 0:
            factor = int(k)
        #print(k, factor)
        for i in range(factor, N, (layersDict[k] - 1) * 2):
            caughtDelays[i] = 1
    #print(caughtDelays)
    for i in range(N):
        if caughtDelays[i] == 0:
            delay = i
            break
    return delay

#print(getSeverity(layersDict))
print(getDelay(layersDict))
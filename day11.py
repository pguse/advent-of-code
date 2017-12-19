inFile = open("hexGridSteps.txt",'r')
s = inFile.read().split(',')

def fewestSteps(steps):
    n = steps.count('n')
    s = steps.count('s')
    ne = steps.count('ne')
    sw = steps.count('sw')
    nw = steps.count('nw')
    se = steps.count('se')

    new_steps = []
    if n > s:
        new_steps = new_steps + ['n']*(n-s)
    else:
        new_steps = new_steps + ['s']*(s-n)
    if ne > sw:
        new_steps = new_steps + ['ne']*(ne-sw)
    else:
        new_steps = new_steps + ['sw']*(sw-ne)
    if nw > se:
        new_steps = new_steps + ['nw']*(nw-se)
    else:
        new_steps = new_steps + ['se']*(se-nw)

    while new_steps.count('ne') > 0 and new_steps.count('nw') > 0:
        new_steps.remove('ne')
        new_steps.remove('nw')
        new_steps.append('n')
    while new_steps.count('se') > 0 and new_steps.count('sw') > 0:
        new_steps.remove('se')
        new_steps.remove('sw')
        new_steps.append('s')
    while new_steps.count('n') > 0 and new_steps.count('s') > 0:
        new_steps.remove('n')
        new_steps.remove('s')
    print(new_steps)
    return len(new_steps)

def mostSteps(steps):
    directions = {'n':0,'s':0,'ne':0,'nw':0,'se':0,'sw':0}
    max_count = 0
    for s in steps:
        directions[s] += 1
        if directions['ne'] > 0 and directions['s'] > 0:
            directions['ne'] -= 1
            directions['s'] -= 1
            directions['se'] += 1  
        if directions['se'] > 0 and directions['n'] > 0:
            directions['se'] -= 1
            directions['n'] -= 1
            directions['ne'] += 1
        if directions['nw'] > 0 and directions['s'] > 0:
            directions['nw'] -= 1
            directions['s'] -= 1
            directions['sw'] += 1  
        if directions['sw'] > 0 and directions['n'] > 0:
            directions['sw'] -= 1
            directions['n'] -= 1
            directions['nw'] += 1                          
        if directions['ne'] > 0 and directions['nw'] > 0:
            directions['ne'] -= 1
            directions['nw'] -= 1
            directions['n'] += 1
        if directions['se'] > 0 and directions['sw'] > 0:
            directions['se'] -= 1
            directions['sw'] -= 1
            directions['s'] += 1
        if directions['n'] > 0 and directions['s'] > 0:
            directions['n'] -= 1
            directions['s'] -= 1
        if directions['ne'] > 0 and directions['sw'] > 0:
            directions['ne'] -= 1
            directions['sw'] -= 1
        if directions['nw'] > 0 and directions['se'] > 0:
            directions['nw'] -= 1
            directions['se'] -= 1
        
        #print(directions)
        count = 0
        for i in directions.values():
            count += i

        if count > max_count:
            max_count = count

    return max_count

print(fewestSteps(s))
print(mostSteps(s))

inFile.close()
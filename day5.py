def numJumps(s):
    sList = [int(n) for n in s.split('\n')]
    index = 0
    count = 0
    while True:
        step = sList[index]
        newIndex = index + step
        count += 1
        if newIndex < 0 or newIndex >= len(sList):
            return count
        else:
            sList[index] += 1
            index = newIndex
def numJumps3(s):
    sList = [int(n) for n in s.split('\n')]
    index = 0
    count = 0
    while True:
        step = sList[index]
        newIndex = index + step
        count += 1
        if newIndex < 0 or newIndex >= len(sList):
            return count
        else:
            if step >= 3:
                sList[index] -= 1
            else:
                sList[index] += 1
            index = newIndex

def test(f, s, result):
    if f(s) != result:
        return False
    else:
        return True

#Tests
print(test(numJumps,"0\n3\n0\n1\n-3",5))
print(test(numJumps3,"0\n3\n0\n1\n-3",10))

#Main
inFile = open("jumps.txt",'r')
jumps = inFile.read()
print(numJumps(jumps))
print(numJumps3(jumps))

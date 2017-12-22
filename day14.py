from day10 import knotHash, denseHash

# Part 1
hexTable = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
inputString = "jzgqcdpd"
rows = []
for i in range(128):
    rows.append(inputString+"-"+str(i))
#print(rows)

rBin = []
count = 0
for i in range(128):
    r = []
    for ch in rows[i]:
        if ch == " ":
            continue
        r.append(ord(ch))
    r = r + [17,31,73,47,23]
    #print(r)

    rKnot = denseHash(knotHash(r))
    #print(rKnot)
    hexList = []
    for n in rKnot:
        hexList.append(hex(n))
    hexString = ""
    for element in hexList:
        if len(element) == 4:
            hexString = hexString + element[2:]
        else:
            hexString = hexString + "0" + element[2]
    #print(hexString)
    binString = ""
    for ch in hexString:
        bStr = str(bin(hexTable[ch])[2:])
        if len(bStr) < 4:
            diff = 4-len(bStr)
            bStr = "0"*diff + bStr
        binString = binString + bStr

    for ch in binString:
        count = count + int(ch)

    rBin.append(binString)

#print(len(rBin))
#print(count)

# Part 2
def findNeighbours(grid, row, col,count):
    grid[row][col] = count
    if row-1 >= 0 and grid[row-1][col] == 1:
        findNeighbours(grid, row-1, col, count)
    if row+1 < len(grid) and grid[row+1][col] == 1:
        findNeighbours(grid, row+1, col,count)
    if col-1 >= 0 and grid[row][col-1] == 1:
        findNeighbours(grid, row, col-1, count)
    if col+1 < len(grid[0]) and grid[row][col+1] == 1:
        findNeighbours(grid, row, col+1, count)

# Create 2D List of Lists
rBinGrid = []
for i in range(len(rBin)):
    rBinGrid.append([])
    for j in range(len(rBin[i])):
        rBinGrid[i].append(int(rBin[i][j]))

#print(rBinGrid)

count = 2
for r in range(len(rBinGrid)):
    for c in range((len(rBinGrid[r]))):
        if rBinGrid[r][c] == 1:
            findNeighbours(rBinGrid, r, c, count)
            count += 1

#print(rBinGrid)
print(count-2)


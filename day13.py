inFile = open("layers.txt",'r')
layers = [ item.split() for item in inFile.read().split('\n') ]

layersDict = {}
for item in layers:
    layersDict[item[0][:-1]] = int(item[1])
print(layersDict)
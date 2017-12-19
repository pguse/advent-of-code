lengths = [14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244]
inFile = open("puzzleLengths.txt",'r')
ascii_lengths = [ord(i) for i in inFile.read()] + [17,31,73,47,23]
inFile.close()

def product(list_of_lengths):
    current_pos = 0
    skip_size = 0
    a = []
    for i in range(256):
        a.append(i)
    for length in list_of_lengths:
        b = []
        for i in range(length):
            b.append(a[ (current_pos+i) % len(a)])
        b = b[::-1]
        index = current_pos
        for j in range(len(b)):
            a[index] = b[j]
            index = (index + 1) % len(a)
        current_pos = (current_pos + length + skip_size) % len(a)
        skip_size += 1
        #print(a, b, current_pos, skip_size)
    return a[0]*a[1]

def knotHash(list_of_lengths):
    current_pos = 0
    skip_size = 0
    a = []
    for i in range(256):
        a.append(i)
    for k in range(64):
        for length in list_of_lengths:
            b = []
            for i in range(length):
                b.append(a[ (current_pos+i) % len(a)])
            b = b[::-1]
            index = current_pos
            for j in range(len(b)):
                a[index] = b[j]
                index = (index + 1) % len(a)
            current_pos = (current_pos + length + skip_size) % len(a)
            skip_size += 1
        #print(a, b, current_pos, skip_size)
    return a

def denseHash(kHash):
    blocks = len(kHash) // 16
    dHash = []
    for j in range(blocks):
        value = kHash[0+16*j]
        for i in range(1+16*j,16+16*j):
            value = value ^ kHash[i]
        dHash.append(value)
    return dHash

#print( product(lengths) )
#print(ascii_lengths)
dHash = denseHash(knotHash(ascii_lengths))
hexList = []
for n in dHash:
    hexList.append(hex(n))
print(hexList)
hexString = ""
for element in hexList:
    if len(element) == 4:
        hexString = hexString + element[2:]
    else:
        hexString = hexString + "0" + element[2]
print(hexString)
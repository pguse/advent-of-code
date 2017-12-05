# Corruption Checksum

def checkSum(s):
    total = 0
    sList = s.split('\n')
    for i in range( len(sList) ):
        sList[i] = [int(n) for n in sList[i].split()]
        largest = sList[i][0]
        smallest = sList[i][0]
        for j in range( len(sList[i]) ):
            if sList[i][j] > largest:
                largest = sList[i][j]
            if sList[i][j] < smallest:
                smallest = sList[i][j]
        total = total + (largest-smallest)
    return total

def sumEvenDivisible(s):
    total = 0
    sList = s.split('\n')
    for i in range( len(sList) ):
        sList[i] = [int(n) for n in sList[i].split()]
        quotient = 0
        for j in range( len(sList[i]) - 1 ):
            for k in range( j+1, len(sList[i]) ):
                if sList[i][j] % sList[i][k] == 0:
                    quotient = sList[i][j] // sList[i][k]
                    break
                elif sList[i][k] % sList[i][j] == 0:
                    quotient = sList[i][k] // sList[i][j]
                    break
        total = total + quotient
    return total

def test(f, s, result):
    if f(s) != result:
        return False
    else:
        return True

#Test
print(test(checkSum,"5\t1\t9\t5\n 7\t5\t3\n 2\t4\t6\t8",18))
print(test(sumEvenDivisible, "5 9 2 8\n9 4 7 3\n3 8 6 5", 9))

#Main
inFile = open("sheet.txt",'r')
sheet = inFile.read()
print(checkSum(sheet))
print(sumEvenDivisible(sheet))
inFile.close()
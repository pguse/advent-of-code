def validPass(s):
    sList = s.split()
    for i in range(len(sList)-1):
        for j in range(i+1,len(sList)):
            if sList[i] == sList[j]:
                return False
    return True

def validPassAnagram(s):
    sList = s.split()
    for i in range(len(sList)-1):
        for j in range(i+1,len(sList)):
            if isAnagram(sList[i],sList[j]):
                return False
    return True

def isAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        for letter in s1:
            if s1.count(letter) != s2.count(letter):
                return False
    return True

def test(f, s, result):
    if f(s) != result:
        return False
    else:
        return True

#Tests
print(test(validPass,"aa bb cc dd ee",True))
print(test(validPass,"aa bb cc dd aa",False))
print(test(validPass,"aa bb cc dd aaa",True))
print(isAnagram("abcde","decab"))
print(isAnagram("aabbcc","abcabc"))
print(isAnagram("aabbcc","abc"))
print(isAnagram("aabbcc","abcdef"))

#Main
inFile = open("passphrases.txt",'r')
pString = inFile.read()
pList = pString.split('\n')
count = 0
for p in pList:
    if validPassAnagram(p):
        count += 1
print(count)
inFile.close()
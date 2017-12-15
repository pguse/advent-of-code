g1 = "{}" # score of 1.
g2 = "{{{}}}" # score of 1 + 2 + 3 = 6.
g3 = "{{},{}}" # score of 1 + 2 + 2 = 5.
g4 = "{{{},{},{{}}}}" # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
g5 = "{<a>,<a>,<a>,<a>}" # score of 1.
g6 = "{{<ab>},{<ab>},{<ab>},{<ab>}}" # score of 1 + 2 + 2 + 2 + 2 = 9.
g7 = "{{<!!>},{<!!>},{<!!>},{<!!>}}" # score of 1 + 2 + 2 + 2 + 2 = 9.
g8 = "{{<a!>},{<a!>},{<a!>},{<ab>}}" # score of 1 + 2 = 3.

def count(stream):
    score = 0
    total = 0
    ch_old = ""
    garbage = False
    for ch in stream:
        if ch_old == "!" and garbage:
            ch_old = ""
            continue
        elif ch == "<" and not garbage:
            garbage = True
        elif ch == ">":
            garbage = False
        elif ch == "{" and ch_old == "," and not garbage:
            total += score
        elif ch == "{" and not garbage:
            score += 1
            total += score
        ch_old = ch
        #print(ch, total, garbage)
    return total

def removeGarbage(stream):
    n = 0
    s = ""
    ch_old = ""
    garbage = False
    for ch in stream:
        if garbage and ch != ">" and ch != "!" and ch_old != "!":
            n += 1
        if ch_old == "!":
            ch_old = ""
            continue
        elif ch == "," and ch_old == ">":
            continue
        elif ch == "<" and not garbage:
            garbage = True
        elif ch == ">":
            garbage = False
        elif garbage == False:
            s = s + ch
        ch_old = ch
    print(n, end = " ")
    return s

def countGroups(stream):
    tally = 0
    total = 0
    for ch in stream:
        if ch == "{":
            tally += 1
            total += tally
        elif ch == "}":
            tally -= 1
        #print(ch, total, garbage)
    return total

# Tests
print( countGroups(removeGarbage(g1)) )
print( countGroups(removeGarbage(g2)) )
print( countGroups(removeGarbage(g3)) )
print( countGroups(removeGarbage(g4)) )
print( countGroups(removeGarbage(g5)) )
print( countGroups(removeGarbage(g6)) )
print( countGroups(removeGarbage(g7)) )
print( countGroups(removeGarbage(g8)) )


inFile = open("characterStream.txt",'r')
s = inFile.read()
print( countGroups(removeGarbage(s)) )
inFile.close()
def spin(p,X):
    for i in range(X):
        p.insert(0,p.pop())

def exchange(p,A,B):
    s = p[A]
    p[A] = p[B]
    p[B] = s

def partner(p,A,B):
    AIndex = p.index(A)
    BIndex = p.index(B)
    s = p[AIndex]
    p[AIndex] = p[BIndex]
    p[BIndex] = s

programs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

#spin(programs,3)
#exchange(programs,3,4)
#partner(programs,'a','c')

#move = 's1'
#move = 'x3/4'
#move = 'pe/b'

inFile = open("danceMoves.txt", 'r')
dance = inFile.read().split(',')
for i in range(1,1000000000):
    for move in dance:
        if move[0] == 's':
            spin(programs,int(move[1:]))
        elif move[0] == 'x':
            indices = move[1:].split('/')
            exchange(programs, int(indices[0]), int(indices[1]))
        elif move[0] == 'p':
            indices = move[1:].split('/')
            partner(programs, indices[0], indices[1])
    permStr =  "".join(programs)
    if permStr == "abcdefghijklmnop" and i != 0:
        break

count = i
for i in range (1000000000 % count):
    for move in dance:
        if move[0] == 's':
            spin(programs,int(move[1:]))
        elif move[0] == 'x':
            indices = move[1:].split('/')
            exchange(programs, int(indices[0]), int(indices[1]))
        elif move[0] == 'p':
            indices = move[1:].split('/')
            partner(programs, indices[0], indices[1])
    
print("".join(programs))

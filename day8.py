def modify(a, cond, b):
    options = { '>': a > b,
                '<': a < b,
                '>=': a >= b,
                '<=': a <= b,
                '==': a == b,
                '!=': a != b}
    return options[cond]

def accum(a, op, value):
    operators = {'inc': a + value,'dec': a - value}
    return operators[op]

# Input instructions from the file
# and store it as a list of instructions
inFile = open('registerInstructions.txt','r')
instructions = inFile.read().split('\n')

# Create a dictionary with keys containing the
# register names and initial values of zero
registers = {}
for i in range(len(instructions)):
    registers[instructions[i].split()[0]] = 0

# Iterate throught the list of instructions
# and imply them to the appropriate registers
# if the condition is true.
highValue = 0
for s in instructions:
    sList = s.split()
    condition = modify(registers[sList[4]],sList[5],int(sList[6]))
    if condition:
        registers[sList[0]] = accum(registers[sList[0]],sList[1],int(sList[2]))
        if registers[sList[0]] > highValue:
            highValue = registers[sList[0]]

print(max(registers.values()))
print("Highest Value: " + str(highValue))
inFile.close()
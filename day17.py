
def part1(step):
    buffer = [0]
    pos = 0
    value = 1
    for i in range(2017):
        pos = (pos + step) % len(buffer)
        pos += 1
        buffer.insert(pos, value)
        value += 1
    return buffer[pos+1]

def part2(step):
    pos = 0
    value = 0
    for i in range(50000000):
        pos = (pos + step) % (i+1)
        if pos == 0:
            value = (i+1)
        pos += 1
        #print(i+1, pos, value)
    return value

#print(part1(324))
print(part2(324))
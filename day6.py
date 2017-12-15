def memAlloc(s):
    s = [int(i) for i in s.split()]

    states = []
    count = 0
    while True:
        count += 1
        maxIndex = 0
        for i in range(1,len(s)):
            if s[i] > s[maxIndex]:
                maxIndex = i

        total = s[maxIndex]
        s[maxIndex] = 0
        i = maxIndex
        while total != 0:
            total -= 1
            i = (i + 1) % len(s)
            s[i] += 1

        s_str = "".join( str(i) for i in s)
        for i in range(len(states)):
            if states[i] == s_str:
                return count, count-i-1
        states.append(s_str)
        #print(states)

banks = "14	 0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
print(memAlloc("0 2 7 0"))
print(memAlloc(banks))
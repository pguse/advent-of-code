def manhatten(n):
    x = 0
    y = 0
    step = 1
    sign = 1
    val = 1
    while val < n:
        val = val + step
        x = x + step*sign
        if val > n:
            x = x - (val-n)*sign
            break
        val = val + step
        y = y + step*sign
        if val > n:
            y = y - (val-n)*sign
            break
        step = step + 1
        sign = sign*(-1)
    return abs(x) + abs(y)

def test(f, s, result):
    if f(s) != result:
        return False
    else:
        return True

print( test(manhatten, 1, 0) )
print( test(manhatten, 12, 3) )
print( test(manhatten, 23, 2) )
print( test(manhatten, 1024, 31) )
print( manhatten(312051) )
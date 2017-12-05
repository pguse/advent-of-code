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

def sumNeighbours(n,size):
    def total(g,i,j):
        return g[i][j-1]+g[i][j+1]+g[i-1][j-1]+g[i-1][j]+g[i-1][j+1]+g[i+1][j-1]+g[i+1][j]+g[i+1][j+1]
    grid = []
    for i in range(size):
        grid.append([0]*size)
    row = size//2
    col = size//2
    grid[row][col] = 1
    step = 1
    stage = 1
    while grid[row][col] <= n:
        count = stage
        while count > 0 and grid[row][col] <= n:
            col = col + step
            grid[row][col] = total(grid,row,col)
            count -= 1
        count = stage
        while count > 0 and grid[row][col] <= n:
            row = row - step
            grid[row][col] = total(grid,row,col)
            count -= 1
        stage += 1
        step *= -1
    return grid[row][col]

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

print(sumNeighbours(312051,50))
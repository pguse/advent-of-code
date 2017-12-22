def my_generator(start, factor, n):
    value = start
    for i in range(n):
        value = value*factor % 2147483647
        yield value

N = 40000000
a = my_generator(65,16807, N)
b = my_generator(8921,48271, N)

count = 0
for i in range(N):
    a_bin = bin(next(a))
    b_bin = bin(next(b))
    a_bin16 = a_bin[len(a_bin)-16:]
    b_bin16 = b_bin[len(b_bin)-16:]
    if a_bin16 == b_bin16:
        count += 1
    #print(a_bin16, b_bin16)
print(count)

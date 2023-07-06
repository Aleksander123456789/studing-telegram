n = 5
m = 5
table = [None]* n

for i in range(n):
    table[i] = [0] * m

for i in range(5):
    for j in range(5):
        if i == j:
            table[i][j] = 1
        else:
            table[i][j] = i + j
print(*table, sep='\n')


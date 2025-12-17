#1
"""
n = int(input("N:"))
fib = [0, 1]
for i in range(n):
    new = fib[0] + fib[1]
    fib[0] = fib[1]
    fib[1] = new
    print(new, fib)
"""
#2
"""
n = int(input("N: "))
jump = [0, 1, 1]
for i in range(n):
    new = jump[0] + jump[1] + jump[2]
    jump[0] = jump[1]
    jump[1] = jump[2]
    jump[2] = new
    print(new,jump)
"""
#3
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1]
]
co = [
    [1, 2, 3,],
    [2, 3, 3],
    [1, 2, 4]
]
path = []
for i in range(len(coins)):
    for j in range(len(coins[i])):
        if j == 0 and i == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j-1]
  
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i-1][j]

        else:
            coins[i][j] = max(coins[i-1][j], coins[i][j-1]) + coins[i][j]
            
    path.append(s)
print(coins[-1][-1])
print(path)


 
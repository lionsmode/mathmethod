#1
"""N = int(input())
if N <= 0:
    print(0)
elif N == 1:
    print(1)
else:
    a, b = 0, 1
    for _ in range(0, N + 1):
        a, b = b, a + b
    print(b)"""
    
    #2
"""n = int(input())
mas = [0] * (n + 1)
mas[0], mas[1] = 1, 1
for i in range(2, n + 1):
    mas[i] = mas[i - 1] + (mas[i - 2] if i - 2 >= 0 else 0) + (mas[i - 3] if i - 3 >= 0 else 0)
    
print(mas[n])"""
#3
"""
coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]
n = 4
m = 6
for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j-1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins [i][j - 0] + coins[i][j])
print(coins[-1][-1])
"""


#1
#1
"""
listr = [6, 2, 5, 4, 2, 5, 6]
n = len(listr)
dp = [1] * n  
for i in range(n):
    for j in range(i):
        if listr[i] > listr[j]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
max_dlina = 0
for dlina in dp:
    if dlina > max_dlina:
        max_dlina = dlina
to_remove = n - max_dlina
print("Последовательность:", listr)
print("максимальный:", max_dlina)
print("удалить минимальное число:", to_remove)

max_index = 0
for i in range(n):
    if dp[i] == max_dlina:
        max_index = i
        break

lis = []
current_dlina = max_dlina
for i in range(max_index, -1, -1):
    if dp[i] == current_dlina:
        lis.append(listr[i])
        current_dlina -= 1
        if current_dlina == 0:
            break

lis.reverse()
print("Пример последовательности:", lis)
"""

#2


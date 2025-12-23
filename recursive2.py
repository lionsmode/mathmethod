#1
"""
def programma(start, end, cherez):
  
    def schitat(ot, do):
        spisok = [0] * (do + 1)
        spisok[ot] = 1
        for i in range(ot, do + 1):
            if i + 1 <= do:
                spisok[i + 1] += spisok[i]
            if i + 2 <= do:
                spisok[i + 2] += spisok[i]
            if i * 2 <= do:
                spisok[i * 2] += spisok[i] 
        return spisok[do]
    
    if cherez < start or cherez > end:
        return 0
   
    return schitat(start, cherez) * schitat(cherez, end)

nachalo = 3
konec = 12
obyazatelnoe = 10
otvet = programma(nachalo, konec, obyazatelnoe)
print(f"Количество: {otvet}")
"""
#2
"""
def solve():
    start = 1
    end = 27
    zapret = 26
    memo = {}
    
    def count_from(x):
        if x > end:
            return 0
        if x == zapret:
            return 0
        if x == end:
            return 1
        if x in memo:
            return memo[x]
        total = 0
        total += count_from(x + 1)
        total += count_from(2 * x + 1)
        memo[x] = total
        return total
    answer = count_from(start)
    print(f"Ответ: {answer}")
    return answer
result = solve()
"""

#3
"""
def proga():
    start = 2
    end = 18
    obyazatelno = 9
    zapret = 14
    
    def count_ot(a, b):
        if a > b or a == zapret:
            return 0
        spisok = [0] * (b + 1)
        spisok[a] = 1  
        for i in range(a, b + 1):
            if i == zapret:
                continue
            if i + 1 <= b:
                spisok[i + 1] += spisok[i]
            if i + 2 <= b:
                spisok[i + 2] += spisok[i]
        
        return spisok[b]
    if obyazatelno < start or obyazatelno > end:
        return 0
    if obyazatelno == zapret:
        return 0
    pervy = count_ot(start, obyazatelno)
    vtoroy = count_ot(obyazatelno, end)
    
    otvet = pervy * vtoroy
    print(f"Ответ: {otvet}")
    return otvet
rezultat = proga()

"""



#обработка символьных строк

#1
"""
with open('27686.txt', 'r') as file:
    s = file.read().strip()
max_len = 0
current_len = 0
for char in s:
    if char == 'X':
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 0

print("Максимальная длина:", max_len)
"""

#2

with open('36037.txt', 'r') as f:
    s = f.read().strip()

max_len = 0



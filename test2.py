"""
import csv

with open("36031.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)-1):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
    print(l)
"""

#zadacha 1
"""
import csv

with open("59778.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    count = 0


    for i in range(len(n)- 1):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i].count(l[i][j]) == 4:
                repeat = l[i][j]
                x = []
                for j in range(len(l[i])):
                    if l[i][j] not in x and l[i][j] != repeat:
                        x.append(l[i][j])
                summa_repeat = 4 * repeat
                average_sum = sum(x) / 3
                if average_sum > summa_repeat:
                    count += 1
    print(count//4)
"""

#zadanie 2
"""
import csv
with open("29666.csv", "r") as file:
    f  = csv.reader(file, delimiter=";")
    l = []
    for i in f:
        a = i[0].replace(",", ".")
        l.append(float(a))
print(l)
sumi = 0
for n in range(len(l)):
    maxi = l[n]
    for n in range(len(l)):
        if l[n] < l[n-1]:
            maxi += l[n]
        else:
            break
    if sumi < maxi:
        sumi = maxi
print(sumi)
"""

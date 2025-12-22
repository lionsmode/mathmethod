#zadacha 1

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
"""

#zadacha 2
"""
def remove_vowels(string):
    glasnie = ['a', 'o', 'e', 'i', 'u', 'y']
    vivod = ''
    for bukva in string:
        if bukva not in glasnie:
            vivod += bukva
    return vivod
n = input()
print(remove_vowels(n))
"""

#zadacha 3

def pascals(n):
    if n == 1:
        return [1]
    x = pascals(n-1)
    row = [1]
    for i in range(len(x) - 1):
        row.append(x[i] + x[i-1])
    row.append(1)
    return row

n = int(input())
print(pascals(n))


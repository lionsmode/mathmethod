#1
"""
def sistema():
    chisla =  "0123456789ABCDE"

    for i in chisla:
        a = int("123" + i + "5", 15)
        b = int("1" + i + "233", 15)
        s = a + b
        
        if s % 14 == 0:
            return s // 14
print(sistema())
"""

#2
"""
def sistema():
    znachenie = "0123456789ABCDEF"  

    num1 = "AB267D1"
    num2 = "F024A89"
    max_znachenie = max(max(int(c, 16) if c.isznachenie() else ord(c) - ord('A') + 10 for c in num1),
                    max(int(c, 16) if c.isznachenie() else ord(c) - ord('A') + 10 for c in num2))
    p = max_znachenie + 1
    while True:
        try:
            a = int(num1, p)
            b = int(num2, p)
        except ValueErro r:
            p += 1
            continue
        s = a + b
        if s % (p - 1) == 0:
            return p
        p += 1
print(sistema())
"""

#3
"""
def sistema():
    for x in range(10):
        num1 = x * (17**4) + 11 * (17**3) + 0 * (17**2) + 9 * (17**1) + 7
        num2 = x * (15**4) + 8 * (15**3) + 14 * (15**2) + 8 * (15**1) + 5
        total = num1 + num2
        
        if total % 155 == 0:
            print(x)
            print(total // 155)
            break

if __name__ == "__sistema__":
    sistema()
"""

#4
"""def sistema():
    x = 0
    y = 0
    mini = 0

    while y < 8:
        while x < 8:
            s = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)

            if s % 117 == 0:
                     mini = s // 117

            x += 1
        x = 0
        y += 1
    return mini
print(sistema())"""

#5
"""def sistema():
    a = 7 * (512 ** 1912)
    b = 6 * (64 ** 1954)
    c = 5 * (8 ** 1991)
    d = 4 * (8 ** 1980)
    value = a + b - c - d - 2022
    value_oct = oct(value)[2:]
    return value_oct.count('7')
otvet = sistema()
print(otvet)"""

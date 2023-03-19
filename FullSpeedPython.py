def math_operation():
    division = 15 / 2
    floor_div = 15 // 2
    modules = 15 % 2
    exponentiation = 15 ** 2

    return [division, floor_div, modules, exponentiation]


[div, f_div, mod, exp] = math_operation()
print(div, "-", f_div, "-", mod, "-", exp)


def checkParity(n):
    return n % 2


print(checkParity(16))


def inRange(x, y):
    return (x < 1 / 3 < y)


print(inRange(2, 3))


def getStr(s):
    new_s = ""
    for i in range(len(s)):
        new_s += s[i] * 3
    return new_s, len(new_s)


print(getStr("abc"))


def findOccurence(s, f):
    index = -1
    find_len = len(f)
    for i in range(len(s)):
        s2 = s[i:i+find_len]
        if s2 == f:
            index = i
            break
    return [index, len(s)]

str = "aabbccx"
find_str = "bbc"
print(findOccurence(str, find_str))

def findOccurance2(s,f):
    index = s.find(f)
    return [index, len(s)]
print(findOccurance2(str,find_str))

def changeCase(s):
    if not s.isupper():
        s = s.upper()
    else:
        s = s.lower()
    return s
print(changeCase('aaa'))
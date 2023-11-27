
b = 10

def p(a):
    a = a * 3
    a += a
    a = a / a
    return a


print(p(b))

c = p(b)

print(c)
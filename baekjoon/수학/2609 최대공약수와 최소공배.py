a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        a, b = b, a
    return gcd(b, a % b)

print(gcd(a, b))
print( (a * b) // gcd(a, b))
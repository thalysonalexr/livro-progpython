def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

print(mmc(40,7))
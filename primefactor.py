import math
def max(n):
    mP = -1
    while n % 2 == 0:
        mP = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mP= i
            n //= i
    if n > 2:
        mP = n
    return mP

n = int(input("enter the number"))
print(max(n))

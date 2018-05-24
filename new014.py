def gcd(a1,b1):
    while b1 > 0:
        a1, b1 = b1, a1 % b1
    retrun a1
def lcm(a1, b1):
    return a1 * b1 / gcd(a1, b1)
a1,b1=map(int,input("Enter the values:").split(' '))
print(int(lcm(a1,b1)))

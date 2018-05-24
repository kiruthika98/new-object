ASCII_SIZE = 256
def getMaxOccuringChar(s1):
    count = [0] * ASCII_SIZE
    max = -1
    c1 = ''
    for i in s1:
        count[ord(i)]+=1;
    for i in s1:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c1 = i
    return c1
s1 =input()
print((getMaxOccuringChar(s1)))


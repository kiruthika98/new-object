try:
    n1,k1 = [int(x) for x in input().split(" ")]
    a = list(map(int,input().split(' ')))
    b= [0]*(2*n)
    for i in range(n1):
        b[i] = a[i]
        b[n1+i] = a[i]
    c=abs(n1-k1)
    print(c,b[c:c+n1])
except:
    print("Invalid Input")


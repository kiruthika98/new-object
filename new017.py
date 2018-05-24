num,k1=map(int,input('Enter Two Number:').split(' '))
if num<k1:
    num,k1=k1,num
print([i for i in range(1,k1+1) if num%i==0 and k1%i==0 ][-1])


x11,y11=map(int,input("Enter !st line").split(' '))
x21,y21=map(int,input("Enter 2nd line").split(' '))
x31,y31=map(int,input("Enter 3rd line").split(' '))
if (x11==x21 and x21==x31) or(y11==y21 and y21==y31) or (abs(x11-x21)==abs(x21-x31) and abs(y11-y21)==abs(y21-y31)): 
print("yes")
else:
print("no")

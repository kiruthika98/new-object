n1 = raw_input().split(" ")
data = [0] + map(int,raw_input().split(" "))
for i in range( int(n1[1]) ):
    pos = map(int,raw_input().split(" "))
    print sum(data[pos[0]:pos[1]+1])


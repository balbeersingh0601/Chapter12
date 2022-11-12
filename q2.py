t=(1,2,3,4,5,6,5,8,7)
l=len(t)
print("Length of tuple",l)
n=int(input("ENter the index value but lesser than length "))
for i in range(l):
    if(i==n):
        print(t[i])

t1=(0,1,1,2,3,5,8)
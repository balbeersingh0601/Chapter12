#Slicing operation
tpl=(10,20,12,13,14,15,30,14,16)
print(tpl[3:30]) #1
print(tpl[-15:7]) #2
print(tpl[0:10:2])#3
print(tpl[::3]) #4
print(tpl[::-3]) #5
print(tpl[5::2])
print(tpl[2:5]*3)

# Joining Operation
tpl1=(1,3,5)
tpl2=(4,5,6)
tpl3=(30,40,50)
print(tpl1+tpl2+tpl3)
print(tpl1+(3,))
print((tpl1*3))

#Comparing Operations
tup=(1,2,3,4,5,6,7,8,9)
t1=tup[2:8:2]
print("t1",t1)
t2=tup[-3:-9:-2]
print("t2",t2)
t3=t2[::-1]
print("t3",t3)
if t3==t1:
    print("The 2 tuples contain the same elements in reversed order")
else:
    print("The 2 tuples contain different elements")

#Deletion
twt=(5,7,3,9,12)
print("twt",twt)
del twt
print("after deletion",twt) #not defined error dega
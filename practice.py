'''
#12.2
t1=tuple(eval(input("Enter the input for tuple 1")))
t2=tuple(eval(input("Enter the input for tuple 2")))
t3=tuple(eval(input("Enter the input for tuple 3")))
print("Tuple 1 :",t1)
print("Tuple 2 :",t2)
print("Tuple 3 :",t3)

#12.6
T=('hello','is','not','python','keyword')
l=len(T)
for a in range(l):
    print("At indexes ",a,"and",(a-l),"element ",T[a])'''

#12.8
tup=eval(input("Enter input for tuple :"))
t1=tup[2:8:2]
t2=tup[-3:-9:-2]
print("Two created tuples are :")
print("Tuple 1: ",t1)
print("Tuple 2 : ",t2)

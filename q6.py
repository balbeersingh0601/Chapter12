t=()
for i in range(2):
    n1=eval((input("Enter the marks of 3 subjects")))
    n2=tuple(n1)
    s=sum(n2)
    print("Total marks obtained is ",s)
    a=s/3
    t+=(n1,)
    print("Marks",n1,"Sum",s,"Average marks", a)
print("Creating a nested tuples for marks of 5 students",t)
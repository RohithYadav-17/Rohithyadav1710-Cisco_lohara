def calc(first:int,second:int):
    sum=first+second
    diff=first-second
    product=first*second
    quotient=first//second
    return sum,diff,product,quotient
s,d,p,q=calc(20,5)
print(s,d,p,q)
t1=calc(10,20)
print(t1)



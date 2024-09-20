'''def find_diff(first:int=1,second:int=2)->int:
    return first-second
print(find_diff(20,10))
print(find_diff(second=10,first=20))
print(find_diff(second=10))
print(find_diff())


def change_name(names,index,name):
    names[index]=name
names=['rahul','rohit','modi']
print(names)
change_name(names,2,'modiji')
print(names)

#multiple return values using tuple packing
print(sum([10,20,30]))'''
#list iterator
#[10,20,30].__iter__()
'''def find_sum(first,second,*others):
    s=first+second
    if(len(others)>0):
        for num in others:
            s+=num
    #print(type(others))
    return s
print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50))'''
#**=dict
'''def find_sum(first,second,**others):
    s=first+second
    if(len(others)>0):
        for key in others:
            s+=others[key]
    #print(type(others))
    return s
print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=30))
print(find_sum(first=10,second=20,third=30,fourth=40,fifth=50))'''
#factorial using recursion
'''def fact(N):
    
    if N<=1:#base/edge case
        return 1
    return N*fact(N-1)
print(fact(5))
print(fact(6))'''

import math
def is_prime(N):
    N_sqrt=int(math.sqrt(N))
    for i in range (2,N_sqrt+1):
        if N%i==0:
            return "Not a prime"
    return "prime"
print(is_prime(5))
print(is_prime(51))
print(is_prime(61))
print(is_prime(60))
print(is_prime(7))






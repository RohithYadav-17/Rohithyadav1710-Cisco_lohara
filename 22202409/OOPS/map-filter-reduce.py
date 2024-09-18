nums=[2,3,4]
#map syntax
#map(<func>,iterable)
num_sqr=list(map(lambda num:num**2,nums))
print(num_sqr)
#filter
nums_even=list(filter(lambda num:num%2==0,nums))
print(nums_even)

#reduce syntax
#reduce(<func>,iterable,init_value)

nums=[10,20,30,41]
from functools import reduce
nums_sum=reduce(lambda s,num:s+num,nums,0)
nums_product=reduce(lambda p,num:p*num,nums,1)
print(nums_sum)
print(nums_product)
#min
nums_min=reduce(lambda a,b:a if a<b else b,nums)
nums_max=reduce(lambda a,b:b if a>b else b,nums)
print(nums_max)
print(nums_min)
'''import sys
nums_min=reduce(lambda m,num:min(m,num),nums,sys.maxsize)
nums_max=reduce(lambda m,num:max(m,num),nums,-sys.maxsize)
nums_min=reduce(min,nums)
nums_max=reduce(max,nums)
print(nums_min,nums_max)'''
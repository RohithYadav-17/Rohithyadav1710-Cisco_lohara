print("enter atleast 5 numbers")
lst=list(map(int,input("enter the numbers").split()))
tup=tuple(lst)
print(f'List:{lst}')
print(f'(Tuple:{tup})')
num_set=set(lst)
num_fset=frozenset(num_set)
dic={i:i**2 for i in lst}
print(f'converted set{num_set}')
print(f'frozen set{num_fset}')
print(f'dictionary of squares{dic}')




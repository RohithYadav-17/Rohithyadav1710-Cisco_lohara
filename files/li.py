lst=list(map(str,input().split()))
tup=tuple(lst)
print(f'List:{lst}')
print(f'(Tuple:{tup})')#file.write(f'List:{lst}\n')
with open('names.txt', 'w') as file:
    file.write("List:"+str(lst)+"\n")
    file.write("tuple:"+str(tup)+"\n")
print('data written to the file')
'''with open('names.txt', 'r') as file:
    line1= file.readline()
    line2= file.readline()
    print(line1)
    print(line2)'''
with open('names.txt', 'r') as file:
    for _ in range(2):
        print(file.readline())




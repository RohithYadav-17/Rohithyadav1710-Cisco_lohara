lst=list(map(str,input().split()))
tup=tuple(lst)
with open('names.txt', 'w') as file:
    file.write("List:"+str(lst)+"\n")
    file.write("tuple:"+str(tup)+"\n")
with open('names.txt', 'r') as file:
    line1= file.readline()
    line2= file.readline()
    print(line1)
    print(line2)
def find_max(a):
    return max(a)


n=int(input("enter number of elements"))
a=[]
for i in range(n):
    num=int(input("enter element"))
    a.append(num)
max_number=find_max(a)
print(max_number)

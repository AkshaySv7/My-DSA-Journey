n = int(input("Number of elements"))
lst = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

unique_lst = list(set(lst))
print("List after removing duplicates:", unique_lst)

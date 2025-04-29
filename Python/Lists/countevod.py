n = int(input("Enter number of elements: "))
nums = []
even = odd = 0

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    nums.append(val)
    if val % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

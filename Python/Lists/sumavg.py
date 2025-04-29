nums = []
print("Enter 10 numbers:")
for i in range(10):
    nums.append(int(input(f"Number {i+1}: ")))

print("Sum:", sum(nums))
print("Average:", sum(nums)/len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))

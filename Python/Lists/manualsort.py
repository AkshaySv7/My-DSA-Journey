def manual_sort(lst, ascending=True):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (ascending and lst[i] > lst[j]) or (not ascending and lst[i] < lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

n = int(input("Enter number of elements: "))
nums = [int(input(f"Element {i+1}: ")) for i in range(n)]

asc = manual_sort(nums.copy(), ascending=True)
desc = manual_sort(nums.copy(), ascending=False)

print("Ascending:", asc)
print("Descending:", desc)

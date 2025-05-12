def most_frequent_char(s):
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

# Example
print(most_frequent_char("hello world"))  # l

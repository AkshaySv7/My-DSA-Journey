def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

# Example
v, c = count_vowels_consonants("Hello World")
print(f"Vowels: {v}, Consonants: {c}")

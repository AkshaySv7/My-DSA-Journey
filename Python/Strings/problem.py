def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

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

def most_frequent_char(s):
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)

# Main program
text = input("Enter a sentence: ")

char_count = len(text.replace(" ", ""))
word_count = len(text.split())
v, c = count_vowels_consonants(text)
most_freq = most_frequent_char(text)
no_duplicates = remove_duplicates(text)
capitalized = capitalize_sentence(text)
palindrome_check = is_palindrome(text)

print("\n--- Text Analysis ---")
print(f"Characters (no spaces): {char_count}")
print(f"Words: {word_count}")
print(f"Vowels: {v}, Consonants: {c}")
print(f"Most frequent character: {most_freq}")
print(f"Without duplicates: {no_duplicates}")
print(f"Capitalized sentence: {capitalized}")
print("Palindrome:", "Yes" if palindrome_check else "No")

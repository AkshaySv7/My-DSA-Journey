def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example
print(is_palindrome("Madam"))  # True

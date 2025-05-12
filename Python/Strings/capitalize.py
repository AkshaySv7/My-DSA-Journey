def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized = [word.capitalize() for word in words]
    return " ".join(capitalized)

# Example
print(capitalize_sentence("hello world from python"))  # Hello World From Python

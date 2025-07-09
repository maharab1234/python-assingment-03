def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
print(longest_word("Python is amazing and powerful"))  
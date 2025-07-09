def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char not in vowels])

# Example
print(remove_vowels("Hello World"))  
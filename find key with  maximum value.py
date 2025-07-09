def max_value_key(d):
    return max(d, key=d.get)

# Example
print(max_value_key({'a': 10, 'b': 50, 'c': 30})) 
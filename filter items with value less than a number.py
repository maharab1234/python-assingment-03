def filter_dict(d, threshold):
    return {k: v for k, v in d.items() if v >= threshold}

# Example
print(filter_dict({'a': 10, 'b': 5, 'c': 15}, 10))
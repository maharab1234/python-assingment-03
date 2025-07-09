def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# Example
print(second_largest([10, 20, 4, 45, 99])) 
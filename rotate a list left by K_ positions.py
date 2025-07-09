def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

# Example
print(rotate_left([1, 2, 3, 4, 5], 2))  
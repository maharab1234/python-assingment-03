def find_repeats(tpl):
    return list(set([x for x in tpl if tpl.count(x) > 1]))

# Example
print(find_repeats((1, 2, 3, 2, 4, 5, 1))) 
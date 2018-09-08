def twins(a, b):
    n = len(a)
    result = []

    for outer_index in range(n):
        odd_a, even_a = [], []
        odd_b, even_b = [], []
        strlen_a = len(a[outer_index])
        strlen_b = len(b[outer_index])
        
        if strlen_a == strlen_b:
            for inner_index in range(strlen_a):
                if inner_index % 2 == 0:
                    odd_a.append(a[outer_index][inner_index])
                    odd_b.append(b[outer_index][inner_index])

                else:
                    even_a.append(a[outer_index][inner_index])
                    even_b.append(b[outer_index][inner_index])

        else:
            result.append('No')
            break
        if (set(odd_a) == set(odd_b)) & (set(even_a) == set(even_b)):
            result.append('Yes')
        else:
            result.append('No')

    return result

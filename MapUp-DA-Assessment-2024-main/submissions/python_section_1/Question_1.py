def reverse_by_n(lst, n):
    result = []
    length = len(lst)
    for i in range(0, length, n):
        group = []
        for j in range(min(n, length - i)):
            group.append(lst[i + n - j - 1])
        result.extend(group)
        
    return result
print(reverse_by_n([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(reverse_by_n([1, 2, 3, 4, 5], 2))  
print(reverse_by_n([10, 20, 30, 40, 50, 60, 70], 4))        
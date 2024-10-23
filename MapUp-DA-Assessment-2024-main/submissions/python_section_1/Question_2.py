# Question 2: Lists & Dictionaries

def group_strings_by_length(lst):
    length_dict = {}
    for string in lst:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = [string]
        else:
            length_dict[length].append(string)
    return dict(sorted(length_dict.items()))
print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group_strings_by_length(["one", "two", "three", "four"]))

def combine_dicts(dict1, dict2):
    result = {}
    for key in dict1.keys():
        if key in dict2.keys():
            result[key] = dict1[key] + dict2[key]
    return result

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
dict2 = {'a':2, 'b':3, 'c':4, 'e':5}
result = combine_dicts(dict1, dict2)
print(result)

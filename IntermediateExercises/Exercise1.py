def get_unique_elements(original_list):
    return list(set(original_list))

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = get_unique_elements(test_list)

print("Original list: ", test_list)
print("Unique elements: ", result)
